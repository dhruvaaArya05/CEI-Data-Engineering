import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()


# Configuration


NUM_CUSTOMERS = 500
NUM_PRODUCTS = 500
NUM_ORDERS = 500
NUM_ORDER_ITEMS = 1000

os.makedirs("data", exist_ok=True)


# Generate Customers


customers = []

customer_types = ["REGULAR", "PREMIUM", "VIP"]

customer_ids = []

for i in range(1, NUM_CUSTOMERS + 1):

    customer_id = f"C{i:04d}"
    customer_ids.append(customer_id)

    email = fake.email()

    # 2% invalid emails
    if random.random() < 0.02:
        invalid_emails = [
            fake.user_name(),
            fake.user_name() + "@",
            fake.user_name() + ".com",
            fake.user_name() + "@gmail"
        ]
        email = random.choice(invalid_emails)

    registration_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    customers.append({
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "email": email,
        "registration_date": registration_date,
        "customer_type": random.choice(customer_types)
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "data/customers.csv",
    index=False
)

print("customers.csv created")


# Generate Products


categories = {
    "Electronics": [
        "Laptop",
        "Mobile",
        "TV",
        "Camera",
        "Speaker"
    ],
    "Clothing": [
        "Shirt",
        "Jeans",
        "Shoes",
        "Jacket",
        "T-Shirt"
    ],
    "Books": [
        "Novel",
        "Biography",
        "Comics",
        "Education",
        "Magazine"
    ],
    "Home": [
        "Chair",
        "Table",
        "Lamp",
        "Sofa",
        "Curtains"
    ]
}

products = []

product_ids = []

for i in range(1, NUM_PRODUCTS + 1):

    product_id = f"P{i:04d}"
    product_ids.append(product_id)

    category = random.choice(list(categories.keys()))
    subcategory = random.choice(categories[category])

    product_name = subcategory

    # Add messy product names
    if random.random() < 0.05:
        styles = [
            product_name.upper(),
            product_name.lower(),
            "   " + product_name,
            product_name + "   ",
            product_name.swapcase()
        ]
        product_name = random.choice(styles)

    cost_price = round(random.uniform(100, 50000), 2)

    products.append({
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "subcategory": subcategory,
        "cost_price": cost_price
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    "data/products.csv",
    index=False
)

print("products.csv created")


# Generate Orders


statuses = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

regions = [
    "NORTH",
    "SOUTH",
    "EAST",
    "WEST"
]

orders = []

order_ids = []

for i in range(1, NUM_ORDERS + 1):

    order_id = f"O{i:04d}"
    order_ids.append(order_id)

    customer = random.choice(customer_ids)

    # 5% NULL customer_id
    if random.random() < 0.05:
        customer = None

    date = fake.date_time_between(
        start_date="-2y",
        end_date="now"
    )

    # Wrong date format
    if random.random() < 0.05:
        order_date = date.strftime("%d-%m-%Y")
    else:
        order_date = date.strftime("%Y-%m-%d %H:%M:%S")

    orders.append({
        "order_id": order_id,
        "customer_id": customer,
        "order_date": order_date,
        "status": random.choice(statuses),
        "region_code": random.choice(regions)
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    "data/orders.csv",
    index=False
)

print("orders.csv created")


# Generate Order Items


order_items = []

for i in range(1, NUM_ORDER_ITEMS + 1):

    quantity = random.randint(1, 5)

    # 3% negative quantity
    if random.random() < 0.03:
        quantity = -random.randint(1, 3)

    order_items.append({

        "item_id": f"I{i:05d}",

        "order_id": random.choice(order_ids),

        "product_id": random.choice(product_ids),

        "quantity": quantity,

        "unit_price": round(
            random.uniform(200, 10000),
            2
        ),

        "discount_percent": round(
            random.uniform(0, 100),
            2
        )
    })

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "data/order_items.csv",
    index=False
)

print("order_items.csv created")

print("\nData generation completed successfully!")