# Databricks notebook source
from pyspark.sql.functions import *
from datetime import datetime

# COMMAND ----------

patients = spark.table("silver.patients")
appointments = spark.table("silver.appointments")
billing = spark.table("silver.billing")
doctors = spark.table("silver.doctors")
treatments = spark.table("silver.treatments")

# COMMAND ----------

patient_count = patients.count()
appointment_count = appointments.count()
billing_count = billing.count()
doctor_count = doctors.count()
treatment_count = treatments.count()

# COMMAND ----------

audit_data = [

(
    datetime.now(),
    patient_count,
    appointment_count,
    billing_count,
    doctor_count,
    treatment_count
)

]

columns = [

"run_time",
"patients_loaded",
"appointments_loaded",
"billing_loaded",
"doctors_loaded",
"treatments_loaded"

]

audit_df = spark.createDataFrame(audit_data, columns)

display(audit_df)

# COMMAND ----------

audit_df.write \
.mode("overwrite") \
.format("delta") \
.saveAsTable("gold.audit_report")

# COMMAND ----------

display(spark.table("gold.audit_report"))

# COMMAND ----------

print("Bronze Tables")
spark.sql("SHOW TABLES IN bronze").show()

print("Silver Tables")
spark.sql("SHOW TABLES IN silver").show()

print("Gold Tables")
spark.sql("SHOW TABLES IN gold").show()