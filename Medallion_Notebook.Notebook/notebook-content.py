# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "309e5b3c-6055-44c4-9af6-a81ba0599936",
# META       "default_lakehouse_name": "Medallion_lakehouse",
# META       "default_lakehouse_workspace_id": "b79aed05-325a-458e-8274-26078b75c2ff",
# META       "known_lakehouses": [
# META         {
# META           "id": "309e5b3c-6055-44c4-9af6-a81ba0599936"
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

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_raw = (
    spark.read
         .schema(sales_schema)
         .option("header", "false")
         .csv(raw_p)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
