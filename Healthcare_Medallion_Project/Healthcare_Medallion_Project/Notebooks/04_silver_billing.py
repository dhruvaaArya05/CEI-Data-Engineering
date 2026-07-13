# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

billing_df = spark.table("bronze.billing")

patients_df = spark.table("silver.patients")

treatments_df = spark.table("bronze.treatments")

# COMMAND ----------

print("Billing Records :", billing_df.count())

display(billing_df)

# COMMAND ----------

billing_df = billing_df.dropDuplicates(["bill_id"])

# COMMAND ----------

billing_df = billing_df.withColumn(
    "bill_date",
    to_date("bill_date", "yyyy-MM-dd")
)

# COMMAND ----------

billing_df = billing_df.withColumn(
    "amount",
    col("amount").cast("double")
)

# COMMAND ----------

billing_df = (
    billing_df
    .withColumn("payment_method", initcap(trim(col("payment_method"))))
    .withColumn("payment_status", initcap(trim(col("payment_status"))))
)

# COMMAND ----------

billing_df = billing_df.join(

    patients_df.select(
        "patient_id",
        "patient_name"
    ),

    on="patient_id",
    how="left"

)

# COMMAND ----------

billing_df = billing_df.join(

    treatments_df.select(
        "treatment_id",
        "treatment_type"
    ),

    on="treatment_id",
    how="left"

)

# COMMAND ----------

billing_df = billing_df.withColumn(

    "billing_status",

    when(col("payment_status") == "Paid", "Completed")
    .when(col("payment_status") == "Pending", "Awaiting Payment")
    .otherwise("Payment Failed")

)

# COMMAND ----------

billing_df = billing_df.withColumn(
    "_silver_load_time",
    current_timestamp()
)

# COMMAND ----------

billing_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.billing")

# COMMAND ----------

display(spark.table("silver.billing"))