# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "c8aba4c8-e9b4-400f-8020-b15f4d0e0266",
# META       "default_lakehouse_name": "medallion_lakehouse",
# META       "default_lakehouse_workspace_id": "c48bbed2-cdef-4f1e-9ff6-04461745e6d4",
# META       "known_lakehouses": [
# META         {
# META           "id": "c8aba4c8-e9b4-400f-8020-b15f4d0e0266"
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
# Load data into pandas DataFrame from "/lakehouse/default/Files/EmployeeData.parquet"
df = pd.read_parquet("/lakehouse/default/Files/EmployeeData.parquet")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/EmployeeData_Update1.parquet"
df = pd.read_parquet("/lakehouse/default/Files/EmployeeData_Update1.parquet")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/EmployeeData_Update2.parquet"
df = pd.read_parquet("/lakehouse/default/Files/EmployeeData_Update2.parquet")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
