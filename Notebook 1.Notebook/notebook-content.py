# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "38480ba8-4fbc-4437-9e51-65a6fb6fc634",
# META       "default_lakehouse_name": "lakehouse_vip1",
# META       "default_lakehouse_workspace_id": "c48bbed2-cdef-4f1e-9ff6-04461745e6d4",
# META       "known_lakehouses": [
# META         {
# META           "id": "38480ba8-4fbc-4437-9e51-65a6fb6fc634"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/data_access/raw/testData.csv"
df = pd.read_csv("/lakehouse/default/Files/data_access/raw/testData.csv")
#display(df)
df.write.mode("overwrite").format("delta").saveAsTable("Tables/shortcut_Table")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/data_access/raw/testData.csv")
# df now is a Spark DataFrame containing CSV data from "Files/data_access/raw/testData.csv".
display(df)
df.write.mode("overwrite").format("delta").saveAsTable("shortcut_Table")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
