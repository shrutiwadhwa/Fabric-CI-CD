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


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/banking_lakehouse/accounts.csv"
df = pd.read_csv("/lakehouse/default/Files/banking_lakehouse/accounts.csv")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
