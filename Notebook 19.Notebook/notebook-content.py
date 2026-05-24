# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "29b159bf-e919-42de-bd04-3ea53ef43aac",
# META       "default_lakehouse_name": "Day2_lakehouse",
# META       "default_lakehouse_workspace_id": "b79aed05-325a-458e-8274-26078b75c2ff",
# META       "known_lakehouses": [
# META         {
# META           "id": "29b159bf-e919-42de-bd04-3ea53ef43aac"
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

df = spark.read.format("csv").option("header","true").load("Files/input/banking_lakehouse/accounts.csv")
# df now is a Spark DataFrame containing CSV data from "Files/input/banking_lakehouse/accounts.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.session.stop()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
