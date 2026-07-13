# 🚀 CEI - Data Engineering Assignment Week-1

## OverView
This Project performs basic data exploration and cleaning using pandas on two datasets:
1. Combined Dataset
2. Ethnic Dataset

## Project Summary
This project focuses on cleaning and preprocessing two datasets using Python and Pandas. The objective was to improve data quality by handling missing values, handling duplicate records, correcting inconsistencies, and preparing the data for further analysis. The cleaned datasets were exported as CSV files for future use in data analysis and machine learning tasks.

## Key Tasks Performed
- Explored data (head / tail, shape, columns, dtypes)
- Identified and handled missing values
- Performed basic operations (filter, select)
- Handled Duplicates
- Created a derived column
- Exported cleaned datasets to CSV format

## Tools Used
- Python
- Pandas
- Jupyter Notebook
- PyCharm

## Outcome
The resulting datasets are cleaner, more consistent, and ready for exploratory data analysis, visualization, or machine learning applications.

# 🚀 CEI - Data Engineering Assignment Week-2

## Overview
This project performs SQL-based data analysis using filtering, aggregation, and basic business queries.
1. e-commerce sales dataset
2. Superset dataset

## Project Summary
The project perform comprehensive sales data analysis using SQL. The analysis focuses on leveraging data filtering, aggregations, and structured business queries to extract actionable insights, evaluate trends, and ensure data quality.

## Key Tasks Performed
- Load dataset into a SQL database
- Explore table (schema, sample data)
- Apply WHERE filters (region, category, date, sales)
- Use GROUP BY for aggregations (sales, quantity, averages)
- Sort and limit results (top products, top categories)
- Solve use cases (monthly trends, top customers, duplicates)
- Validate results (row counts, data quality)

## Tools Used
- SQL
- MySQL Workbench
- Pandas
- Jupyter Notebook
- PyCharm

## Outcome
The Final submission consists of SQL script, executed query results, and a summary of brief business insights.

# 🚀 CEI - Data Engineering Assignment Week-3

## Overview
A SQL-based sales analysis project that transforms raw Superstore data into business insights using three core techniques: 
Subqueries
CTEs
Window Functions

## Key Tasks Performed
- Load the Superstore dataset into a superstore_raw table
- Create structured tables: customers, orders, products
- Populate tables using SELECT DISTINCT
- Apply subqueries to filter above-average sales and find each customer's highest order
- Use CTEs to compute total sales per customer
- Apply window functions (ROW_NUMBER, RANK) for ranking
- Combine JOIN + CTE + Window Functions for a final result showing customer, total sales, and rank
- Answer business queries: top customers, low customers, single-order customers, above-average sales

## Outcome
A SQL script or notebook with query results and brief insights.

# 🚀 CEI - Data Engineering Assignment Week-4

## Overview
Build an end-to-end data pipeline on Azure using Storage Account and Azure Data Factory (ADF), while understanding core Azure cloud concepts.

## Project Summary
This is a hands-on cloud data engineering project that walks through setting up a complete data ingestion and transformation pipeline on Microsoft Azure — from raw file storage to pipeline execution and monitoring.

## Key Tasks Performed
- Azure Portal Setup
- Storage Configuration
- ADF Setup
- Linked Dataset and Services
- IAM & Access Control

# 🚀 CEI - Data Engineering Assignment Week-5

## Overview
This project focuses on learning Apache Spark DataFrames and performing data cleaning, transformation, filtering, and aggregation on large datasets. It highlights Spark's advantages over MapReduce, including faster in-memory processing and efficient distributed computing.

## Project Summary
Built a data processing pipeline using PySpark to clean and transform data, handle duplicates and null values, manage schemas, perform filtering and aggregations, and generate insights through grouped analysis. The project also explored Spark concepts such as immutability, shuffle operations, and wide transformations.

## Key Tasks Performed
- Removed duplicate records and handled null values.
- Applied filters based on age, category, region, and subscription type.
- Renamed and dropped columns as part of data cleaning.
- Cast columns to appropriate data types (e.g., timestamps).
- Performed aggregations using count, sum, avg, min, and max.
- Used groupBy() for category-wise and city-wise analysis.
- Built an end-to-end Spark DataFrame processing pipeline.
- Studied shuffle operations and DataFrame immutability concepts.

## Tools Used
- Apache Spark
- PySpark
- Spark DataFrames
- Python

# 🚀 CEI - Data Engineering Assignment Week-7

## Overview
Perform incremental data processing using Delta Lake.

## Dataset
- customer_master.csv
- customer_incremental.csv

## Key Tasks Performed
- Loaded source datasets.
- Removed nulls and duplicates.
- Created a Delta table from the master dataset.
- Performed Delta MERGE operation.
- Updated existing records.
- Inserted new records.
- Validated final row count and output.

## Tools Used
- Databricks
- Apache Spark
- Delta Lake

# E-Commerce Order Analytics System Week-8

## Project Overview

This project is an E-Commerce Order Analytics System developed using **Python**, **Pandas**, and **SQLite**. It simulates an online shopping platform by generating sample data, cleaning and validating it, storing it in a SQLite database, and generating business reports using SQL queries.

This project was developed as part of an internship mini project to demonstrate data processing, database management, and SQL analysis skills.

---

## Technologies Used

- Python
- Pandas
- Faker
- SQLite3

---

## Project Structure

```
E-Commerce System/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── order_items.csv
│
├── cleaned/
│   ├── customers_clean.csv
│   ├── products_clean.csv
│   ├── orders_clean.csv
│   ├── order_items_clean.csv
│   ├── invalid_emails.csv
│   ├── invalid_order_items.csv
│   └── issues_report.txt
│
|
│── ecommerce.db
│
├── scripts/
│   ├── queries.py
│   ├── report.py
│   └── tests.py
│
│── data_generator.py
│── clean_data.py
│── load_db.py
│
└── README.md
```

---

## Features

### 1. Data Generation

The application generates four CSV files containing sample e-commerce data.

- Customers
- Products
- Orders
- Order Items

The generated data also includes intentional data quality issues such as:

- Missing customer IDs
- Invalid email addresses
- Incorrect date formats
- Negative quantities
- Product names with inconsistent formatting

---

### 2. Data Cleaning

The cleaning module performs the following tasks:

- Converts incorrect date formats
- Handles missing customer IDs
- Removes duplicate records
- Normalizes product names
- Validates customer email addresses
- Checks referential integrity
- Generates an issues report

---

### 3. Database Creation

The cleaned CSV files are loaded into a SQLite database.

Database Tables:

- customers
- products
- orders
- order_items

---

### 4. SQL Analysis

The project includes SQL queries for business analysis such as:

- Total revenue by category
- Top 10 customers
- Monthly order count
- Return rate analysis
- Running totals
- Product ranking
- Customer segmentation
- Year-over-Year comparison
- Cohort analysis
- Frequently bought together products

---

### 5. Reporting

The command-line reporting tool allows users to generate reports based on a selected date range.

The report displays:

- Total orders
- Revenue
- Unique customers
- Top 3 products
- Revenue comparison with previous period

---

### 6. Testing

The project includes edge-case tests for:

- Invalid Order IDs
- Discount greater than 100%
- Zero quantity
- Future order dates

---

## How to Run the Project

### Step 1

Install the required libraries

```bash
pip install pandas faker
```

---

### Step 2

Generate sample data

```bash
python scripts/data_generator.py
```

---

### Step 3

Clean the generated data

```bash
python scripts/clean_data.py
```

---

### Step 4

Load the cleaned data into SQLite

```bash
python scripts/load_db.py
```

---

### Step 5

Run SQL queries

Open the SQLite database (`database/ecommerce.db`) using DB Browser for SQLite or execute the SQL queries from the `sql/queries.sql` file.

---

### Step 6

Generate reports

```bash
python scripts/report.py
```

---

### Step 7

Run test cases

```bash
python scripts/tests.py
```

---

## Learning Outcomes

This project demonstrates:

- Python programming
- Data generation using Faker
- Data cleaning with Pandas
- Data validation
- SQLite database operations
- SQL joins and aggregations
- Window functions
- Common Table Expressions (CTEs)
- Business reporting
- Basic software testing

---

Intern Mini Project – E-Commerce Order Analytics System

# Healthcare Medallion Architecture using Databricks (Major Project)

## Project Overview

This project demonstrates the implementation of a Medallion Architecture (Bronze, Silver, and Gold layers) using Databricks, PySpark, and Delta Lake for a healthcare management system.

The project ingests raw healthcare data from multiple CSV files, cleans and transforms the data, and creates business-ready datasets for reporting and analytics.

---

## Technology Stack

- Databricks Free Edition
- Apache Spark (PySpark)
- Delta Lake
- Unity Catalog
- SQL
- Python

---

## Dataset

The project uses five healthcare datasets:

- Patients
- Appointments
- Doctors
- Treatments
- Billing

---

## Project Architecture

```
CSV Files
     │
     ▼
Bronze Layer
(Raw Data)
     │
     ▼
Silver Layer
(Cleansed & Enriched Data)
     │
     ▼
Gold Layer
(Business KPIs & Reporting)
```

---

## Bronze Layer

The Bronze layer stores the raw source data without business transformations.

### Tasks Performed

- Read CSV files
- Metadata-driven ingestion
- Added ingestion timestamp
- Added batch ID
- Added source file information
- Stored data as Delta tables

### Bronze Tables

- bronze.patients
- bronze.appointments
- bronze.billing
- bronze.doctors
- bronze.treatments

---

## Silver Layer

The Silver layer cleans and enriches the raw data.

### Patients

- Removed duplicate records
- Trimmed text fields
- Standardized email addresses
- Converted dates
- Created patient full name

### Appointments

- Removed duplicates
- Converted appointment dates
- Joined with Patients
- Joined with Doctors
- Created doctor full name

### Billing

- Removed duplicates
- Converted bill dates
- Converted amount to numeric
- Standardized payment status
- Joined with Patients
- Joined with Treatments

### Doctors

- Removed duplicates
- Cleaned text columns
- Converted years of experience
- Created doctor full name

### Treatments

- Removed duplicates
- Converted treatment cost
- Converted treatment date
- Joined with appointment information

---

## Gold Layer

The Gold layer provides business-ready datasets.

### KPIs Created

- Total Patients
- Appointment Status Summary
- Total Revenue
- Revenue by Payment Method
- Revenue by Treatment Type
- Top Doctors by Appointments
- Monthly Revenue
- Dashboard Summary

---

## Audit Report

An audit report was created to summarize pipeline execution.

It includes:

- Pipeline run time
- Number of patients processed
- Number of appointments processed
- Number of billing records
- Number of doctors
- Number of treatments

---

## Project Structure

```
Healthcare_Medallion_Project/

│
├── 00_setup_config
├── 01_ingest_bronze
├── 02_silver_patients
├── 03_silver_appointments
├── 04_silver_billing
├── 05_silver_doctors_treatments
├── 06_gold_kpis
└── 07_audit_report
```

---

## Business Benefits

- Centralized healthcare data
- Improved data quality
- Faster reporting
- Reliable business KPIs
- Scalable data pipeline using Medallion Architecture

---

Healthcare Medallion Architecture Project

Built using Databricks, PySpark, and Delta Lake.

## Author
Dhruva Keshav Arya - Data Engineering Intern @ Celebal Technologies
