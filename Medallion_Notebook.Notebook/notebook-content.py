# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "65c64077-03c4-4d84-a532-b2e9090e784b",
# META       "default_lakehouse_name": "Medallion_laksehouse",
# META       "default_lakehouse_workspace_id": "c48bbed2-cdef-4f1e-9ff6-04461745e6d4",
# META       "known_lakehouses": [
# META         {
# META           "id": "65c64077-03c4-4d84-a532-b2e9090e784b"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# =============================================================================
# Notebook 01 - BRONZE LAYER
# Lakehouse: lh_sales_medallion
# Purpose:   Land raw CSV files into a Delta table, append-only, no business
#            logic. Add ingestion metadata so we never lose provenance.
# =============================================================================

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



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_path = "abfss://c48bbed2-cdef-4f1e-9ff6-04461745e6d4@onelake.dfs.fabric.microsoft.com/65c64077-03c4-4d84-a532-b2e9090e784b/Files/Bronze"

df_raw = (
    spark.read
         .schema(sales_schema)
         .option("header", "false")
         .csv(raw_path)
)

# -----------------------------------------------------------------------------
# 3. Add Bronze metadata. This is the ONE thing we do at Bronze.
#    Everything else stays raw.
# -----------------------------------------------------------------------------
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

df = spark.sql("""
    SELECT _source_file, COUNT(*) AS row_count
    FROM   bronze_sales
    GROUP  BY _source_file
    ORDER  BY _source_file
""")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
