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

# MARKDOWN ********************

# # Lab 0 — Environment & seed data
# **Manual:** Lab 0  •  **Prereq:** Lakehouse `lh_deepdive` attached as the default lakehouse.
# 
# Builds the dataset every later notebook depends on, including a deliberately fragmented table for the tuning labs.

# MARKDOWN ********************

# ## 0.2  Confirm your runtime defaults
# Record these — they drive Lab 5 and the Capstone.

# CELL ********************

print("Spark version :", spark.version)
print("Resource profile:", spark.conf.get("spark.fabric.resourceProfile", "<unset>"))
print("V-Order default :", spark.conf.get("spark.sql.parquet.vorder.default", "<unset>"))
print("AQE enabled     :", spark.conf.get("spark.sql.adaptive.enabled"))
print("Shuffle parts   :", spark.conf.get("spark.sql.shuffle.partitions"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# > **Watch out:** in workspaces created after April 2025 the `writeHeavy` profile sets `spark.sql.parquet.vorder.default = false`. V-Order is **off** by default. You exploit this in Lab 5.

# MARKDOWN ********************

# ## 0.3  Generate the seed dataset
# Skew is planted on purpose: `vendor_id = 1` holds ~70% of rows.

# CELL ********************

from pyspark.sql import functions as F

ROWS = 12_00  # scale down to 2_000_000 on Trial capacity if needed

trips = (spark.range(0, ROWS)
    .withColumn("trip_id", F.col("id"))
    .withColumn("vendor_id",
        F.when(F.rand(7) < 0.70, F.lit(1))
         .when(F.rand(7) < 0.85, F.lit(2)).otherwise(F.lit(3)))
    .withColumn("pickup_zone", (F.col("id") % 265 + 1).cast("int"))
    .withColumn("dropoff_zone", (F.rand(1) * 265 + 1).cast("int"))
    .withColumn("passengers", (F.rand(2) * 5 + 1).cast("int"))
    .withColumn("distance_km", F.round(F.rand(3) * 40 + 0.5, 2))
    .withColumn("fare", F.round(F.col("distance_km") * 1.8 + F.rand(4) * 5, 2))
    .withColumn("pickup_ts",
        (F.lit(1704067200) + (F.rand(5) * 31_536_000)).cast("timestamp"))
    .drop("id"))

trips.write.format("delta").mode("overwrite").saveAsTable("trips")

zones = (spark.range(1, 266)
    .withColumnRenamed("id", "zone_id")
    .withColumn("borough",
        F.element_at(F.array(*[F.lit(b) for b in
          ["Centre","North","South","East","West"]]),
          (F.col("zone_id") % 5 + 1).cast("int")))
    .withColumn("zone_name", F.concat(F.lit("Zone-"), F.col("zone_id"))))
zones.write.format("delta").mode("overwrite").saveAsTable("zones")

print("trips:", spark.table("trips").count(), " zones:", spark.table("zones").count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## 0.4  Plant the small-file problem
# Feeds the small-file diagnostics in Lab 4 and the Capstone.

# CELL ********************

(spark.table("trips")
    .repartition(800)
    .write.format("delta").mode("overwrite")
    .saveAsTable("trips_fragmented"))

files = spark.sql("DESCRIBE DETAIL trips_fragmented").select("numFiles","sizeInBytes").first()
print("numFiles:", files["numFiles"], " avg MB/file:",
      round(files["sizeInBytes"] / files["numFiles"] / 1024 / 1024, 2))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Checkpoint:** `trips` ≈ 12M rows, `zones` = 265, and `trips_fragmented` has hundreds of tiny files.
