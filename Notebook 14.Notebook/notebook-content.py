# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "affb2433-fd2f-4def-bee3-4f7e0ef30644",
# META       "default_lakehouse_name": "Day1Lakehouse",
# META       "default_lakehouse_workspace_id": "b79aed05-325a-458e-8274-26078b75c2ff",
# META       "known_lakehouses": [
# META         {
# META           "id": "affb2433-fd2f-4def-bee3-4f7e0ef30644"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.read.format("csv").option("header", "true").load("")
df.write.format("delta").mode("overwrite").saveAsTable("my_delta_table")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
