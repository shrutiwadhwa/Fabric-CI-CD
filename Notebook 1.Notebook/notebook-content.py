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
# META           "id": "d66ebfa3-5a54-41b0-9efe-f59d003baae6"
# META         },
# META         {
# META           "id": "affb2433-fd2f-4def-bee3-4f7e0ef30644"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "default_warehouse": "db1e07f4-062d-48cf-9e76-63223c7dcc5c",
# META       "known_warehouses": [
# META         {
# META           "id": "db1e07f4-062d-48cf-9e76-63223c7dcc5c",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
customers_df = spark.read.option("header", True).option("inferSchema", True).csv("abfss://b79aed05-325a-458e-8274-26078b75c2ff@onelake.dfs.fabric.microsoft.com/d66ebfa3-5a54-41b0-9efe-f59d003baae6/Files/banking_lakehouse/customers.csv")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(customers_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customers_df.write.mode("overwrite").format("delta").saveAsTable("customers")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv") \
    .option("header", "true") \
    .load("Files/dirty_transaction_data.csv")

display(df)

df.write \
    .mode("overwrite") \
    .format("delta") \
    .save("/delta/dirty_transaction_data")

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

# CELL ********************

accounts_df = spark.read.option("header", True).option("inferSchema", True).csv("Files/banking/raw/accounts/accounts.csv")
transactions_df = spark.read.option("header", True).option("inferSchema", True).csv("Files/banking/raw/transactions/transactions.csv")
branches_df = spark.read.option("header", True).option("inferSchema", True).csv("Files/banking/raw/branches/branches.csv")
loans_df = spark.read.option("header", True).option("inferSchema", True).csv("Files/banking/raw/loans/loans.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# /lakehouse/default/Files/banking_lakehouse
