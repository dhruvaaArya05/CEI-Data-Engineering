import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("../ecommerce.db")
cursor = conn.cursor()

print("=" * 50)
print(" E-Commerce Analytics Report ")
print("=" * 50)

print("\nSelect Report Type")
print("1. Daily")
print("2. Weekly")
print("3. Monthly")

choice = input("\nEnter your choice (1/2/3): ")

start_date = input("Enter Start Date (YYYY-MM-DD): ")
end_date = input("Enter End Date (YYYY-MM-DD): ")

print("\nGenerating Report...\n")

# Total Orders

query = """
SELECT COUNT(*)
FROM orders
WHERE DATE(order_date)
BETWEEN ? AND ?
"""

cursor.execute(query, (start_date, end_date))
orders = cursor.fetchone()[0]

print("Total Orders :", orders)

# Revenue

query = """
SELECT ROUND(

SUM(

quantity * unit_price *

(1-discount_percent/100)

),2)

FROM order_items oi

JOIN orders o

ON oi.order_id=o.order_id

WHERE DATE(order_date)

BETWEEN ? AND ?

AND quantity>0
"""

cursor.execute(query, (start_date, end_date))

revenue = cursor.fetchone()[0]

print("Revenue :", revenue)

# Unique Customers

query = """
SELECT COUNT(DISTINCT customer_id)

FROM orders

WHERE DATE(order_date)

BETWEEN ? AND ?
"""

cursor.execute(query, (start_date, end_date))

customers = cursor.fetchone()[0]

print("Unique Customers :", customers)

# Top 3 Products

print("\nTop 3 Products\n")

query = """
SELECT

p.product_name,

SUM(oi.quantity) AS total_quantity

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

JOIN orders o

ON oi.order_id=o.order_id

WHERE DATE(order_date)

BETWEEN ? AND ?

AND oi.quantity>0

GROUP BY p.product_name

ORDER BY total_quantity DESC

LIMIT 3
"""

cursor.execute(query, (start_date, end_date))

rows = cursor.fetchall()

for row in rows:
    print(row[0], "-", row[1])

# Previous Period Comparison

print("\nPrevious Period Comparison")

query = """
SELECT

ROUND(

SUM(

quantity*unit_price*

(1-discount_percent/100)

),2)

FROM order_items oi

JOIN orders o

ON oi.order_id=o.order_id

WHERE DATE(order_date)<?
"""

cursor.execute(query, (start_date,))

previous = cursor.fetchone()[0]

if previous is None:
    previous = 0

if revenue is None:
    revenue = 0

if previous > 0:

    change = ((revenue - previous) / previous) * 100

    print("Revenue Change :", round(change, 2), "%")

else:

    print("No previous data available.")

conn.close()

print("\nReport Generated Successfully.")