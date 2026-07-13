# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

doctors_df = spark.table("bronze.doctors")

display(doctors_df)

# COMMAND ----------

doctors_df = doctors_df.dropDuplicates(["doctor_id"])

# COMMAND ----------

doctors_df = (
    doctors_df
    .withColumn("first_name", trim(col("first_name")))
    .withColumn("last_name", trim(col("last_name")))
    .withColumn("specialization", trim(col("specialization")))
    .withColumn("hospital_branch", trim(col("hospital_branch")))
    .withColumn("email", lower(trim(col("email"))))
)

# COMMAND ----------

doctors_df = doctors_df.withColumn(
    "years_experience",
    col("years_experience").cast("int")
)

# COMMAND ----------

doctors_df = doctors_df.withColumn(
    "doctor_name",
    concat_ws(" ", col("first_name"), col("last_name"))
)

# COMMAND ----------

doctors_df = doctors_df.withColumn(
    "_silver_load_time",
    current_timestamp()
)

# COMMAND ----------

doctors_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.doctors")

# COMMAND ----------

treatments_df = spark.table("bronze.treatments")

appointments_df = spark.table("silver.appointments")

# COMMAND ----------

treatments_df = treatments_df.dropDuplicates(["treatment_id"])

# COMMAND ----------

treatments_df = (
    treatments_df
    .withColumn("cost", col("cost").cast("double"))
    .withColumn("treatment_date", to_date("treatment_date", "yyyy-MM-dd"))
)

# COMMAND ----------

treatments_df = treatments_df.join(

    appointments_df.select(
        "appointment_id",
        "patient_id",
        "doctor_id",
        "patient_name",
        "doctor_name"
    ),

    on="appointment_id",
    how="left"

)

# COMMAND ----------

treatments_df = treatments_df.withColumn(
    "treatment_type",
    initcap(trim(col("treatment_type")))
)

# COMMAND ----------

treatments_df = treatments_df.withColumn(
    "_silver_load_time",
    current_timestamp()
)

# COMMAND ----------

treatments_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.treatments")

# COMMAND ----------

display(spark.table("silver.doctors"))

# COMMAND ----------

display(spark.table("silver.treatments"))