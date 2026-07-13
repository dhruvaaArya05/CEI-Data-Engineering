# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

spark.sql("CREATE DATABASE IF NOT EXISTS bronze")
spark.sql("CREATE DATABASE IF NOT EXISTS silver")
spark.sql("CREATE DATABASE IF NOT EXISTS gold")

# COMMAND ----------

spark.sql("SHOW DATABASES").show()

# COMMAND ----------

DATA_PATH = "/Volumes/workspace/default/healthcare_data"

# COMMAND ----------

from pyspark.sql import Row

metadata = [
    Row(
        source_id="SRC001",
        source_name="patients",
        file_path=f"{DATA_PATH}/patients.csv",
        target_table="bronze.patients",
        load_type="FULL",
        active_flag="Y"
    ),
    Row(
        source_id="SRC002",
        source_name="appointments",
        file_path=f"{DATA_PATH}/appointments.csv",
        target_table="bronze.appointments",
        load_type="FULL",
        active_flag="Y"
    ),
    Row(
        source_id="SRC003",
        source_name="billing",
        file_path=f"{DATA_PATH}/billing.csv",
        target_table="bronze.billing",
        load_type="FULL",
        active_flag="Y"
    ),
    Row(
        source_id="SRC004",
        source_name="doctors",
        file_path=f"{DATA_PATH}/doctors.csv",
        target_table="bronze.doctors",
        load_type="FULL",
        active_flag="Y"
    ),
    Row(
        source_id="SRC005",
        source_name="treatments",
        file_path=f"{DATA_PATH}/treatments.csv",
        target_table="bronze.treatments",
        load_type="FULL",
        active_flag="Y"
    )
]

metadata_df = spark.createDataFrame(metadata)

display(metadata_df)

# COMMAND ----------

metadata_df.write \
    .mode("overwrite") \
    .saveAsTable("metadata_config")

# COMMAND ----------

spark.sql("""
CREATE TABLE IF NOT EXISTS audit_log (
    audit_id STRING,
    batch_id STRING,
    source_name STRING,
    layer STRING,
    pipeline_start_time TIMESTAMP,
    pipeline_end_time TIMESTAMP,
    rows_read LONG,
    rows_written LONG,
    status STRING,
    error_message STRING
)
USING DELTA
""")