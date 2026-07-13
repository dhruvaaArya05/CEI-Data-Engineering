# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

appointments_df = spark.table("bronze.appointments")

patients_df = spark.table("silver.patients")

doctors_df = spark.table("bronze.doctors")

# COMMAND ----------

print("Appointments :", appointments_df.count())

display(appointments_df)

# COMMAND ----------

appointments_df = appointments_df.dropDuplicates(["appointment_id"])

# COMMAND ----------

appointments_df = appointments_df.withColumn(
    "appointment_date",
    to_date("appointment_date", "yyyy-MM-dd")
)

# COMMAND ----------

appointments_df = appointments_df.join(

    patients_df.select(
        "patient_id",
        "patient_name",
        "gender"
    ),

    on="patient_id",
    how="left"

)

# COMMAND ----------

appointments_df = appointments_df.join(

    doctors_df.select(
        "doctor_id",
        "first_name",
        "last_name",
        "specialization"
    ),

    on="doctor_id",
    how="left"

)

# COMMAND ----------

appointments_df = appointments_df.withColumn(

    "doctor_name",

    concat_ws(
        " ",
        col("first_name"),
        col("last_name")
    )

)

# COMMAND ----------

appointments_df = appointments_df.drop(
    "first_name",
    "last_name"
)

# COMMAND ----------

appointments_df = appointments_df.withColumn(
    "status",
    initcap(trim(col("status")))
)

# COMMAND ----------

appointments_df = appointments_df.withColumn(
    "_silver_load_time",
    current_timestamp()
)

# COMMAND ----------

appointments_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.appointments")

# COMMAND ----------

display(spark.table("silver.appointments"))