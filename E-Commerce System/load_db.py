import sqlite3
import pandas as pd

print("Connecting to SQLite Database...")

# Create database
conn = sqlite3.connect("ecommerce.db")

cursor = conn.cursor()

# Read cleaned CSV files
customers = pd.read_csv("cleaned/customers_clean.csv")
products = pd.read_csv("cleaned/products_clean.csv")
orders = pd.read_csv("cleaned/orders_clean.csv")
order_items = pd.read_csv("cleaned/order_items_clean.csv")

# ---------------------------------------
# Create Tables
# ---------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    customer_id TEXT,
    customer_name TEXT,
    email TEXT,
    registration_date TEXT,
    customer_type TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    subcategory TEXT,
    cost_price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id TEXT,
    customer_id TEXT,
    order_date TEXT,
    status TEXT,
    region_code TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items(
    item_id TEXT,
    order_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    unit_price REAL,
    discount_percent REAL
)
""")

conn.commit()

print("Tables created successfully.\n")

# ---------------------------------------
# Load Data into SQLite
# ---------------------------------------

customers.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

order_items.to_sql(
    "order_items",
    conn,
    if_exists="replace",
    index=False
)

print("Data inserted successfully.\n")

# ---------------------------------------
# Verify Data
# ---------------------------------------

tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]

for table in tables:

    query = f"SELECT COUNT(*) FROM {table}"

    cursor.execute(query)

    total = cursor.fetchone()[0]

    print(f"{table} : {total} records")

conn.close()

print("\nDatabase Created Successfully.")