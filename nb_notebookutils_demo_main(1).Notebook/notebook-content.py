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

import pandas as pd

wrangler_sample_df = pd.read_csv("https://aka.ms/wrangler/titanic.csv")
display(wrangler_sample_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "editable": true
# META }

# CELL ********************

import pandas as pd

wrangler_sample_df = pd.read_csv("https://aka.ms/wrangler/titanic.csv")
display(wrangler_sample_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "editable": false
# META }

# MARKDOWN ********************

# ## nb_notebookutils_demo_main
# 
# New notebook

# MARKDOWN ********************

# # NotebookUtils Example Notebook

# CELL ********************

# MAGIC %%sh
# MAGIC ls

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_notebookutils_demo_main

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Section 1: `notebookutils.fs`

# MARKDOWN ********************

# #### `help()`

# CELL ********************

notebookutils.fs.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.help('fastcp')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `ls()`

# CELL ********************

notebookutils.fs.ls("Files")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `mkdirs()`

# CELL ********************

notebookutils.fs.mkdirs('Files/demo_folder_1')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `notebookutils.fs.cp`

# CELL ********************

notebookutils.fs.cp('Files/demo_folder_1/animals.csv','Files/demo_folder_2/animals_copied.csv',False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Azure Blob Storage access using `notebookutils.fs`

# CELL ********************

notebookutils.fs.ls("abfss://input@shruadls.dfs.core.windows.net/")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.head("abfss://input@shruadls.dfs.core.windows.net/customers.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Section 2: `notebookutils.notebook`

# MARKDOWN ********************

# ### `help()`

# CELL ********************

notebookutils.notebook.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `exit()`

# CELL ********************

notebookutils.notebook.help("exit")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.exit("some string value")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `run()`

# CELL ********************

notebookutils.notebook.help("run")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

exit_value = notebookutils.notebook.run("nb_notebookutils_demo_sub_1", 60, {"param1": "Hello World!"})
print(exit_value)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `runMultiple()`

# CELL ********************

notebookutils.notebook.help("runMultiple")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.runMultiple(["nb_notebookutils_demo_sub_1", "nb_notebookutils_demo_sub_2"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

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

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `list()`

# CELL ********************

notebookutils.notebook.help("list")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.list()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `create()`

# CELL ********************

notebookutils.notebook.help("create")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

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

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.create("nb_notebookutils_demo_create_test_123", "random description", notebook_content)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `delete()`

# CELL ********************

notebookutils.notebook.help("delete")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.delete("nb_notebookutils_demo_create_test_123")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Section 3: `notebookutils.lakehouse`

# CELL ********************

notebookutils.lakehouse.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `list()`

# CELL ********************

notebookutils.lakehouse.list()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `get()`

# CELL ********************

notebookutils.lakehouse.get("shrulake")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `getWithProperties()`

# CELL ********************

notebookutils.lakehouse.getWithProperties("shrulake")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Section 4: `notebookutils.credentials`

# MARKDOWN ********************

# ### `help()`

# CELL ********************

notebookutils.credentials.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `getSecret()`

# CELL ********************

secret_value = notebookutils.credentials.getSecret('https://ap-fabric-kv-dev.vault.azure.net/', 'test-secret')
print(secret_value)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

str(list(secret_value))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Section 5: `notebookutils.runtime`

# CELL ********************

notebookutils.runtime.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### `context`

# CELL ********************

ctx=notebookutils.runtime.context
print(ctx["currentWorkspaceName"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
