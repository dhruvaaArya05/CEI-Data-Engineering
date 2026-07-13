# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
import uuid
from datetime import datetime

# COMMAND ----------

metadata_df = spark.table("metadata_config")
display(metadata_df)

# COMMAND ----------

batch_id = str(uuid.uuid4())

print(batch_id)

# COMMAND ----------

from pyspark.sql.functions import *

for row in metadata_df.collect():

    source = row["source_name"]
    path = row["file_path"]
    target = row["target_table"]

    print(f"Loading {source}...")

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(path)
    )

    bronze_df = (
        df
        .withColumn("_ingestion_timestamp", current_timestamp())
        .withColumn("_source_file_name", lit(source))
        .withColumn("_batch_id", lit(batch_id))
        .withColumn("_layer", lit("BRONZE"))
        .withColumn("_pipeline_version", lit("1.0"))
    )

    bronze_df.write \
        .mode("overwrite") \
        .format("delta") \
        .saveAsTable(target)

    print(f"{source} loaded successfully.")

# COMMAND ----------

spark.sql("SHOW TABLES IN bronze").show(truncate=False)

# COMMAND ----------

display(spark.table("bronze.patients"))