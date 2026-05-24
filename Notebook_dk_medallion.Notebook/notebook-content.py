# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "91b7a0a8-1006-4901-9219-7c1c0f425796",
# META       "default_lakehouse_name": "dk_lake",
# META       "default_lakehouse_workspace_id": "b79aed05-325a-458e-8274-26078b75c2ff",
# META       "known_lakehouses": [
# META         {
# META           "id": "91b7a0a8-1006-4901-9219-7c1c0f425796"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

from pyspark.sql import functions as F
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, DoubleType
)

# -----------------------------------------------------------------------------
# 1. Define schema explicitly. The CSVs have NO header row, so we must.
#    Senior-DE note: explicit schema beats inferSchema every time -
#    it is faster, reproducible, and fails loudly on drift.
# -----------------------------------------------------------------------------
sales_schema = StructType([
    StructField("SalesOrderNumber",     StringType(),  True),
    StructField("SalesOrderLineNumber", IntegerType(), True),
    StructField("OrderDate",            StringType(),  True),   # cast to date in Silver
    StructField("CustomerName",         StringType(),  True),
    StructField("EmailAddress",         StringType(),  True),
    StructField("Item",                 StringType(),  True),
    StructField("Quantity",             IntegerType(), True),
    StructField("UnitPrice",            DoubleType(),  True),
    StructField("TaxAmount",            DoubleType(),  True),
])

df_raw = (
    spark.read
         .schema(sales_schema)
         .option("header", "false")
         .csv("abfss://b79aed05-325a-458e-8274-26078b75c2ff@onelake.dfs.fabric.microsoft.com/91b7a0a8-1006-4901-9219-7c1c0f425796/Files/raw_data_bronz/*.csv")
)

df_bronze = (
    df_raw
    .withColumn("_ingest_ts",   F.current_timestamp())
    .withColumn("_source_file", F.input_file_name())
)

# -----------------------------------------------------------------------------
# 4. Write as a managed Delta table. Overwrite for idempotent lab runs.
#    In production you would use mode("append") with a watermark.
# -----------------------------------------------------------------------------
(
    df_bronze.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("bronze_sales")
)

# -----------------------------------------------------------------------------
# 5. Validate
# -----------------------------------------------------------------------------
print(f"Bronze row count: {spark.table('bronze_sales').count():,}")
spark.table("bronze_sales").show(5, truncate=False)
spark.sql("""
    SELECT _source_file, COUNT(*) AS row_count
    FROM   bronze_sales
    GROUP  BY _source_file
    ORDER  BY _source_file
""").show(truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import functions as F

# -----------------------------------------------------------------------------
# 1. Read Bronze
# -----------------------------------------------------------------------------
df_b = spark.read.table("bronze_sales")

# -----------------------------------------------------------------------------
# 2. Conform types + split the Item field into ProductName and Size.
#    The Item field has two shapes:
#       - "Mountain-100 Silver, 44"   -> ProductName + Size
#       - "Water Bottle - 30 oz."     -> ProductName only, no size
#    We handle both with a single split + size check.
# -----------------------------------------------------------------------------
df_silver = (
    df_b
    # Drop bronze-only metadata before promoting to silver
    .drop("_ingest_ts", "_source_file")

    # Type casts
    .withColumn("OrderDate", F.to_date(F.col("OrderDate")))

    # Split Item -> ProductName + Size (Size = 'N/A' when no comma present)
    .withColumn("_parts", F.split(F.col("Item"), ", ", 2))
    .withColumn("ProductName", F.trim(F.col("_parts").getItem(0)))
    .withColumn(
        "Size",
        F.when(F.size("_parts") > 1, F.trim(F.col("_parts").getItem(1)))
         .otherwise(F.lit("N/A"))
    )
    .drop("_parts", "Item")

    # Business derivations
    .withColumn("LineTotal",   F.round(F.col("Quantity") * F.col("UnitPrice"), 2))
    .withColumn("GrossAmount", F.round(F.col("LineTotal") + F.col("TaxAmount"), 2))

    # Calendar derivations (handy for Silver consumers; Gold can re-derive)
    .withColumn("OrderYear",    F.year("OrderDate"))
    .withColumn("OrderMonth",   F.month("OrderDate"))
    .withColumn("OrderQuarter", F.quarter("OrderDate"))

    # Audit
    .withColumn("_silver_load_ts", F.current_timestamp())

    # Deduplicate on the natural primary key
    .dropDuplicates(["SalesOrderNumber", "SalesOrderLineNumber"])
)

# -----------------------------------------------------------------------------
# 3. Data Quality checks. Fail fast - never let bad data into Silver.
# -----------------------------------------------------------------------------
bad_pk_null  = df_silver.filter(
    F.col("SalesOrderNumber").isNull() | F.col("SalesOrderLineNumber").isNull()
).count()
bad_qty      = df_silver.filter(F.col("Quantity") <= 0).count()
bad_price    = df_silver.filter(F.col("UnitPrice") < 0).count()
bad_date     = df_silver.filter(F.col("OrderDate").isNull()).count()

print(f"DQ -> null PK rows : {bad_pk_null}")
print(f"DQ -> bad quantity : {bad_qty}")
print(f"DQ -> negative price: {bad_price}")
print(f"DQ -> bad dates    : {bad_date}")

assert bad_pk_null == 0, "Null PK found - aborting Silver write"
assert bad_qty     == 0, "Non-positive quantity found - aborting Silver write"
assert bad_price   == 0, "Negative price found - aborting Silver write"
assert bad_date    == 0, "Unparseable OrderDate found - aborting Silver write"

# -----------------------------------------------------------------------------
# 4. Write Silver as a managed Delta table
# -----------------------------------------------------------------------------
(
    df_silver.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("silver_sales")
)

# -----------------------------------------------------------------------------
# 5. Optimize for downstream Gold reads
# -----------------------------------------------------------------------------
spark.sql("OPTIMIZE silver_sales")

# -----------------------------------------------------------------------------
# 6. Validate
# -----------------------------------------------------------------------------
print(f"\nSilver row count: {spark.table('silver_sales').count():,}")
spark.table("silver_sales").select(
    "SalesOrderNumber","OrderDate","CustomerName","ProductName","Size",
    "Quantity","UnitPrice","LineTotal","GrossAmount"
).show(5, truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import functions as F
from pyspark.sql.window import Window

# -----------------------------------------------------------------------------
# 1. Read Silver
# -----------------------------------------------------------------------------
df_s = spark.read.table("silver_sales")

# =============================================================================
# DIMENSION TABLES
# =============================================================================

# -----------------------------------------------------------------------------
# 1.1 dim_product - one row per (ProductName, Size). Surrogate key assigned.
# -----------------------------------------------------------------------------
w_prod = Window.orderBy("ProductName", "Size")

dim_product = (
    df_s.select("ProductName", "Size").distinct()
        .withColumn("ProductKey", F.row_number().over(w_prod))
        .select("ProductKey", "ProductName", "Size")
)

(dim_product.write.format("delta").mode("overwrite")
    .option("overwriteSchema","true").saveAsTable("dim_product"))

# -----------------------------------------------------------------------------
# 1.2 dim_customer - one row per customer (by email as natural key)
# -----------------------------------------------------------------------------
w_cust = Window.orderBy("EmailAddress")

dim_customer = (
    df_s.select("CustomerName", "EmailAddress").distinct()
        .withColumn("CustomerKey", F.row_number().over(w_cust))
        .select("CustomerKey", "CustomerName", "EmailAddress")
)

(dim_customer.write.format("delta").mode("overwrite")
    .option("overwriteSchema","true").saveAsTable("dim_customer"))

# -----------------------------------------------------------------------------
# 1.3 dim_date - generated calendar covering the full Silver range
# -----------------------------------------------------------------------------
date_bounds = df_s.agg(
    F.min("OrderDate").alias("min_d"),
    F.max("OrderDate").alias("max_d")
).collect()[0]

dim_date = (
    spark.sql(f"""
        SELECT explode(
            sequence(
                to_date('{date_bounds['min_d']}'),
                to_date('{date_bounds['max_d']}'),
                interval 1 day
            )
        ) AS OrderDate
    """)
    .withColumn("DateKey",   F.date_format("OrderDate", "yyyyMMdd").cast("int"))
    .withColumn("Year",      F.year("OrderDate"))
    .withColumn("Month",     F.month("OrderDate"))
    .withColumn("MonthName", F.date_format("OrderDate", "MMMM"))
    .withColumn("Quarter",   F.quarter("OrderDate"))
    .withColumn("DayName",   F.date_format("OrderDate", "EEEE"))
    .select("DateKey","OrderDate","Year","Quarter","Month","MonthName","DayName")
)

(dim_date.write.format("delta").mode("overwrite")
    .option("overwriteSchema","true").saveAsTable("dim_date"))

# =============================================================================
# FACT TABLE
# =============================================================================

# -----------------------------------------------------------------------------
# 2. fact_sales - one row per sales order line, with surrogate keys joined in.
# -----------------------------------------------------------------------------
fact_sales = (
    df_s
    .join(dim_product,
          on=["ProductName", "Size"], how="left")
    .join(dim_customer,
          on=["CustomerName", "EmailAddress"], how="left")
    .join(dim_date.select("OrderDate", "DateKey"),
          on="OrderDate", how="left")
    .select(
        "SalesOrderNumber",
        "SalesOrderLineNumber",
        "DateKey",
        "CustomerKey",
        "ProductKey",
        "Quantity",
        "UnitPrice",
        "TaxAmount",
        "LineTotal",
        "GrossAmount"
    )
)

(fact_sales.write.format("delta").mode("overwrite")
    .option("overwriteSchema","true").saveAsTable("fact_sales"))

# =============================================================================
# AGGREGATED MARTS (optional, but great for fast dashboards)
# =============================================================================

# -----------------------------------------------------------------------------
# 3.1 Monthly sales mart
# -----------------------------------------------------------------------------
monthly_sales_mart = (
    df_s.groupBy("OrderYear", "OrderMonth")
        .agg(
            F.countDistinct("SalesOrderNumber").alias("OrderCount"),
            F.sum("Quantity").alias("UnitsSold"),
            F.round(F.sum("LineTotal"), 2).alias("Revenue"),
            F.round(F.sum("TaxAmount"), 2).alias("Tax"),
            F.round(F.sum("GrossAmount"), 2).alias("GrossAmount")
        )
        .orderBy("OrderYear", "OrderMonth")
)

(monthly_sales_mart.write.format("delta").mode("overwrite")
    .option("overwriteSchema","true").saveAsTable("mart_monthly_sales"))

# -----------------------------------------------------------------------------
# 3.2 Top products mart
# -----------------------------------------------------------------------------
top_products_mart = (
    df_s.groupBy("ProductName")
        .agg(
            F.countDistinct("SalesOrderNumber").alias("OrderCount"),
            F.sum("Quantity").alias("UnitsSold"),
            F.round(F.sum("LineTotal"), 2).alias("Revenue")
        )
        .orderBy(F.desc("Revenue"))
)

(top_products_mart.write.format("delta").mode("overwrite")
    .option("overwriteSchema","true").saveAsTable("mart_top_products"))

# -----------------------------------------------------------------------------
# 4. Optimize Gold tables (helps Direct Lake performance)
# -----------------------------------------------------------------------------
for t in ["dim_product","dim_customer","dim_date","fact_sales",
          "mart_monthly_sales","mart_top_products"]:
    spark.sql(f"OPTIMIZE {t}")

# -----------------------------------------------------------------------------
# 5. Validate
# -----------------------------------------------------------------------------
print(f"dim_product        : {spark.table('dim_product').count():,} rows")
print(f"dim_customer       : {spark.table('dim_customer').count():,} rows")
print(f"dim_date           : {spark.table('dim_date').count():,} rows")
print(f"fact_sales         : {spark.table('fact_sales').count():,} rows")
print(f"mart_monthly_sales : {spark.table('mart_monthly_sales').count():,} rows")
print(f"mart_top_products  : {spark.table('mart_top_products').count():,} rows")

print("\n--- Top 5 products by revenue ---")
spark.table("mart_top_products").show(5, truncate=False)

print("\n--- Monthly revenue (first 6 months) ---")
spark.table("mart_monthly_sales").show(6, truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
