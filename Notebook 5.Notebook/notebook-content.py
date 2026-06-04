# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a43cc85c-5827-4061-a570-37ba63476133",
# META       "default_lakehouse_name": "lakehouse_vip",
# META       "default_lakehouse_workspace_id": "c48bbed2-cdef-4f1e-9ff6-04461745e6d4",
# META       "known_lakehouses": [
# META         {
# META           "id": "a43cc85c-5827-4061-a570-37ba63476133"
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

df = spark.read.parquet("Files/EmployeeData_Update2.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/EmployeeData_Update2.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
