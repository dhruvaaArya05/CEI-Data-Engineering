import pandas as pd
from datetime import datetime

# Load cleaned data
orders = pd.read_csv("cleaned/orders_clean.csv")
order_items = pd.read_csv("cleaned/order_items_clean.csv")


# Test 1: Invalid Order IDs

def test_invalid_order_id():

    print("\nTest 1 : Invalid Order IDs")

    valid_orders = set(orders["order_id"])

    invalid = order_items[
        ~order_items["order_id"].isin(valid_orders)
    ]

    if len(invalid) == 0:
        print("PASS : No invalid order IDs found.")
    else:
        print("FAIL : Invalid order IDs found.")
        print(invalid)


# Test 2: Discount > 100

def test_discount():

    print("\nTest 2 : Discount > 100")

    invalid = order_items[
        order_items["discount_percent"] > 100
    ]

    if len(invalid) == 0:
        print("PASS : All discounts are valid.")
    else:
        print("FAIL : Invalid discounts found.")
        print(invalid)



# Test 3: Quantity = 0

def test_quantity_zero():

    print("\nTest 3 : Quantity = 0")

    invalid = order_items[
        order_items["quantity"] == 0
    ]

    if len(invalid) == 0:
        print("PASS : No zero quantity found.")
    else:
        print("FAIL : Zero quantity exists.")
        print(invalid)


# Test 4: Future Order Dates

def test_future_dates():

    print("\nTest 4 : Future Order Dates")

    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )

    today = datetime.today()

    future = orders[
        orders["order_date"] > today
    ]

    if len(future) == 0:
        print("PASS : No future order dates.")
    else:
        print("FAIL : Future order dates found.")
        print(future)


# Main Program

print("=" * 50)
print("Running Edge Case Tests")
print("=" * 50)

test_invalid_order_id()
test_discount()
test_quantity_zero()
test_future_dates()

print("\nAll tests completed.")