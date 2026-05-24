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


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/test_sortcut/banking_lakehouse/customers.csv"
df = pd.read_csv("/lakehouse/default/Files/test_sortcut/banking_lakehouse/customers.csv")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%spark
# MAGIC df = spark.read.format("csv").option("header","true").load("Files/test_sortcut/banking_lakehouse/loans.csv")
# MAGIC # df now is a Spark DataFrame containing CSV data from "Files/test_sortcut/banking_lakehouse/loans.csv".
# MAGIC display(df)
# MAGIC df = df.withColumn("new_roi",col("interest_rate"))

# METADATA ********************

# META {
# META   "language": "scala",
# META   "language_group": "synapse_pyspark"
# META }
