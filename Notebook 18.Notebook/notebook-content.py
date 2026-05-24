# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d66ebfa3-5a54-41b0-9efe-f59d003baae6",
# META       "default_lakehouse_name": "TavantLake",
# META       "default_lakehouse_workspace_id": "b79aed05-325a-458e-8274-26078b75c2ff",
# META       "known_lakehouses": [
# META         {
# META           "id": "d66ebfa3-5a54-41b0-9efe-f59d003baae6"
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

df = spark.read.format("csv").option("header","true").load("Files/input/transactions.csv")
# df now is a Spark DataFrame containing CSV data from "Files/input/transactions.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
