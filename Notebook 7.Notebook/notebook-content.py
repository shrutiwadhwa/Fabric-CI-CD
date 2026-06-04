# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "9ee7ff38-e85c-4d0d-a749-6f131dbc583f",
# META       "default_lakehouse_name": "shrulake",
# META       "default_lakehouse_workspace_id": "c48bbed2-cdef-4f1e-9ff6-04461745e6d4",
# META       "known_lakehouses": [
# META         {
# META           "id": "9ee7ff38-e85c-4d0d-a749-6f131dbc583f"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
#!/usr/bin/env python
# coding: utf-8

# ## nb_notebookutils_demo_main
# 
# New notebook

# # NotebookUtils Example Notebook

# In[3]:


notebookutils.help()


# # Section 1: `notebookutils.fs`

# #### `help()`

# In[4]:


notebookutils.fs.help()


# In[5]:


notebookutils.fs.help('fastcp')


# ### `ls()`
# 

# In[6]:


notebookutils.fs.ls("Files")


# ### `mkdirs()`

# In[7]:


notebookutils.fs.mkdirs('Files/demo_folder_2')


# ### `notebookutils.fs.cp`

# In[8]:


notebookutils.fs.cp('Files/demo_folder_1/animals.csv','Files/demo_folder_2/animals_copied.csv',False)


# ### Azure Blob Storage access using `notebookutils.fs`

# In[9]:


notebookutils.fs.ls("abfss://datalake@apfabricstdldev.dfs.core.windows.net/temp")


# In[10]:


notebookutils.fs.head("abfss://datalake@apfabricstdldev.dfs.core.windows.net/temp/file_in_azure_data_lake.txt")


# # Section 2: `notebookutils.notebook`

# ### `help()`
# 

# In[11]:


notebookutils.notebook.help()


# ### `exit()`

# In[14]:


notebookutils.notebook.help("exit")


# In[15]:


notebookutils.notebook.exit("some string value")


# ### `run()`
# 

# In[16]:


notebookutils.notebook.help("run")


# In[17]:


exit_value = notebookutils.notebook.run("nb_notebookutils_demo_sub_1", 60, {"param1": "Hello World!"})
print(exit_value)


# ### `runMultiple()`

# In[19]:


notebookutils.notebook.help("runMultiple")


# In[20]:


notebookutils.notebook.runMultiple(["nb_notebookutils_demo_sub_1", "nb_notebookutils_demo_sub_2"])


# In[21]:


# run multiple notebooks with parameters
DAG = {
    "activities": [
        {
            "name": "nb_notebookutils_demo_sub_1", # activity name, must be unique
            "path": "nb_notebookutils_demo_sub_1", # notebook path
            "timeoutPerCellInSeconds": 90, # max timeout for each cell, default to 90 seconds
            "retry": 1, # retry amount
            "retryIntervalInSeconds": 10, # retry interval in seconds
            "args": {"param1": "Hello World!"} # notebook parameters
        },
        {
            "name": "nb_notebookutils_demo_sub_2",
            "path": "nb_notebookutils_demo_sub_2"
        },
        {
            "name": "nb_notebookutils_demo_sub_3",
            "path": "nb_notebookutils_demo_sub_3",
            "timeoutPerCellInSeconds": 120,
            "dependencies": ["nb_notebookutils_demo_sub_2"] # list of activity names that this activity depends on
        }
    ],
    "timeoutInSeconds": 43200, # max timeout for the entire pipeline, default to 12 hours
    "concurrency": 50 # max number of notebooks to run concurrently, default to 50, 0 means unlimited
}
notebookutils.notebook.runMultiple(DAG, {"displayDAGViaGraphviz": True})


# ### `list()`

# In[22]:


notebookutils.notebook.help("list")


# In[23]:


notebookutils.notebook.list()


# ### `create()`

# In[24]:


notebookutils.notebook.help("create")


# In[25]:


notebook_content =  {
	"cells": [
		{
			"cell_type": "code",
			"source": [
				"print(\"abc\")"
			],
			"outputs": [],
			"execution_count": None,
			"metadata": {
				"microsoft": {
					"language": "python",
					"language_group": "synapse_pyspark"
				}
			},
			"id": "abe16427-3af0-41bb-b1fd-7d05fb9e8185"
		},
		{
			"cell_type": "code",
			"source": [
				"notebookutils.notebook.exit(\"exit value!\")"
			],
			"outputs": [],
			"execution_count": None,
			"metadata": {
				"jupyter": {
					"source_hidden": False,
					"outputs_hidden": False
				},
				"nteract": {
					"transient": {
						"deleting": False
					}
				},
				"microsoft": {
					"language": "python",
					"language_group": "synapse_pyspark"
				}
			},
			"id": "667e03d1-86b8-403a-baa2-989c98642d31"
		}
	],
	"metadata": {
		"kernel_info": {
			"name": "synapse_pyspark"
		},
		"kernelspec": {
			"name": "synapse_pyspark",
			"display_name": "synapse_pyspark"
		},
		"language_info": {
			"name": "python"
		},
		"microsoft": {
			"language": "python",
			"language_group": "synapse_pyspark",
			"ms_spell_check": {
				"ms_spell_check_language": "en"
			}
		},
		"widgets": {},
		"nteract": {
			"version": "nteract-front-end@1.0.0"
		},
		"spark_compute": {
			"compute_id": "/trident/default"
		},
		"dependencies": {}
	},
	"nbformat": 4,
	"nbformat_minor": 5
}


# In[26]:


notebookutils.notebook.create("nb_notebookutils_demo_create_test_123", "random description", notebook_content)


# ### `delete()`

# In[28]:


notebookutils.notebook.help("delete")


# In[29]:


notebookutils.notebook.delete("nb_notebookutils_demo_create_test_123")


# # Section 3: `notebookutils.lakehouse`

# In[30]:


notebookutils.lakehouse.help()


# ### `list()`

# In[31]:


notebookutils.lakehouse.list()


# ### `get()`

# In[32]:


notebookutils.lakehouse.get("lh_aleksi_fabric_demo_02")


# ### `getWithProperties()`

# In[33]:


notebookutils.lakehouse.getWithProperties("lh_aleksi_fabric_demo_02")


# # Section 4: `notebookutils.credentials`

# ### `help()`

# In[34]:


notebookutils.credentials.help()


# ### `getSecret()`

# In[35]:


secret_value = notebookutils.credentials.getSecret('https://ap-fabric-kv-dev.vault.azure.net/', 'test-secret')
print(secret_value)


# In[36]:


str(list(secret_value))


# # Section 5: `notebookutils.runtime`

# In[38]:


notebookutils.runtime.help()


# ### `context`

# In[39]:


notebookutils.runtime.context



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
