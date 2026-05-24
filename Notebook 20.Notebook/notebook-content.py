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

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/data-access/banking_lakehouse/customers.csv"
df = pd.read_csv("/lakehouse/default/Files/data-access/banking_lakehouse/customers.csv")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
