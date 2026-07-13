# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

patients_df = spark.table("bronze.patients")

display(patients_df)

# COMMAND ----------

print("Rows before cleaning :", patients_df.count())

# COMMAND ----------

patients_df = patients_df.dropDuplicates(["patient_id"])

# COMMAND ----------

string_columns = [
    "first_name",
    "last_name",
    "gender",
    "address",
    "insurance_provider",
    "insurance_number",
    "email"
]

for column in string_columns:
    patients_df = patients_df.withColumn(column, trim(col(column)))

# COMMAND ----------

patients_df = (
    patients_df
    .withColumn(
        "date_of_birth",
        to_date(col("date_of_birth"), "yyyy-MM-dd")
    )
    .withColumn(
        "registration_date",
        to_date(col("registration_date"), "yyyy-MM-dd")
    )
)

# COMMAND ----------

patients_df = patients_df.withColumn(
    "contact_number",
    regexp_replace("contact_number", "[^0-9]", "")
)

# COMMAND ----------

patients_df = patients_df.withColumn(
    "patient_name",
    concat_ws(" ", col("first_name"), col("last_name"))
)

# COMMAND ----------

patients_df = patients_df.filter(col("patient_id").isNotNull())

# COMMAND ----------

patients_df = (
    patients_df
    .withColumn("_silver_load_time", current_timestamp())
    .withColumn("_data_quality", lit("PASS"))
)

# COMMAND ----------

patients_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.patients")

# COMMAND ----------

display(spark.table("silver.patients"))