# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

patients_df = spark.table("silver.patients")
appointments_df = spark.table("silver.appointments")
billing_df = spark.table("silver.billing")
doctors_df = spark.table("silver.doctors")
treatments_df = spark.table("silver.treatments")

# COMMAND ----------

total_patients = patients_df.select(countDistinct("patient_id").alias("total_patients"))

display(total_patients)

# COMMAND ----------

total_patients.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.total_patients")

# COMMAND ----------

appointment_summary = appointments_df.groupBy("status") \
    .count() \
    .withColumnRenamed("count", "total_appointments")

display(appointment_summary)

# COMMAND ----------

appointment_summary.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.appointment_summary")

# COMMAND ----------

total_revenue = billing_df.select(
    round(sum("amount"), 2).alias("total_revenue")
)

display(total_revenue)

# COMMAND ----------

total_revenue.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.total_revenue")

# COMMAND ----------

payment_summary = billing_df.groupBy("payment_method") \
    .agg(
        round(sum("amount"),2).alias("total_revenue")
    ) \
    .orderBy(desc("total_revenue"))

display(payment_summary)

# COMMAND ----------

payment_summary.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.revenue_by_payment")

# COMMAND ----------

treatment_summary = treatments_df.groupBy("treatment_type") \
    .agg(
        round(sum("cost"),2).alias("revenue")
    ) \
    .orderBy(desc("revenue"))

display(treatment_summary)

# COMMAND ----------

treatment_summary.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.revenue_by_treatment")

# COMMAND ----------

top_doctors = appointments_df.groupBy(
    "doctor_name",
    "specialization"
).count() \
.orderBy(desc("count"))

display(top_doctors)

# COMMAND ----------

top_doctors.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.top_doctors")

# COMMAND ----------

monthly_revenue = billing_df.withColumn(
    "month",
    date_format("bill_date","yyyy-MM")
).groupBy("month") \
.agg(
    round(sum("amount"),2).alias("revenue")
) \
.orderBy("month")

display(monthly_revenue)

# COMMAND ----------

monthly_revenue.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.monthly_revenue")

# COMMAND ----------

dashboard_summary = spark.sql("""

SELECT

    (SELECT COUNT(*) FROM silver.patients) AS total_patients,

    (SELECT COUNT(*) FROM silver.doctors) AS total_doctors,

    (SELECT COUNT(*) FROM silver.appointments) AS total_appointments,

    (SELECT COUNT(*) FROM silver.treatments) AS total_treatments,

    (SELECT ROUND(SUM(amount),2) FROM silver.billing) AS total_revenue

""")

display(dashboard_summary)

# COMMAND ----------

dashboard_summary.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold.dashboard_summary")

# COMMAND ----------

spark.sql("SHOW TABLES IN gold").show(truncate=False)