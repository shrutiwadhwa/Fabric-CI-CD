# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   }
# META }

# CELL ********************

#!/usr/bin/env python
# coding: utf-8

# ## nb_fabric_de_series_028_main_2
# 
# New notebook

# In[1]:


notebookutils.notebook.run("nb_fabric_de_series_028_sub_1", 90, {"param_1": "some param_1 value here!"})


# In[2]:


print_this("abc")


# In[3]:


exit_value = notebookutils.notebook.run("nb_fabric_de_series_028_sub_1", 90, {"param_1": "some param_1 value here!"})
print(exit_value)


# In[4]:


exit_values = notebookutils.notebook.runMultiple(["nb_fabric_de_series_028_sub_1", "nb_fabric_de_series_028_sub_2"])
print(exit_values)


# In[5]:


print(exit_values["1"]["exitVal"])


# In[6]:


# run multiple notebooks with parameters
DAG = {
    "activities": [
        {
            "name": "nb_fabric_de_series_028_sub_1", # activity name, must be unique
            "path": "nb_fabric_de_series_028_sub_1", # notebook path
            "timeoutPerCellInSeconds": 90, # max timeout for each cell, default to 90 seconds
            "args": {"param_1": "this is param_1 value!"}, # notebook parameters
            "retry": 1,
            "retryIntervalInSeconds": 10
        },
        {
            "name": "nb_fabric_de_series_028_sub_2",
            "path": "nb_fabric_de_series_028_sub_2",
            "args": {"param_1": "this is param_1 value!"}
        },
        {
            "name": "nb_fabric_de_series_028_sub_3",
            "path": "nb_fabric_de_series_028_sub_3",
            "timeoutPerCellInSeconds": 90,
            "args": {"param_1": "this is param_1 value!"},
            "retry": 1,
            "retryIntervalInSeconds": 10,
            "dependencies": ["nb_fabric_de_series_028_sub_1","nb_fabric_de_series_028_sub_2"] # list of activity names that this activity depends on
        }
    ],
    "timeoutInSeconds": 300, # max timeout for the entire DAG, default to 12 hours
    "concurrency": 3 # max number of notebooks to run concurrently, default to 50
}
exit_values_dag = notebookutils.notebook.runMultiple(DAG, {"displayDAGViaGraphviz": True})
print(exit_values_dag)


# In[7]:


print(exit_values_dag["nb_fabric_de_series_028_sub_3"]["exitVal"])


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.run("nb_fabric_de_series_028_sub_1", 90, {"param_1": "some param_1 value here!"})



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print_this("abc")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
