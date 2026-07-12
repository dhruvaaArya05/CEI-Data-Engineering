import pandas as pd
import os
import re

# Create output folder if it doesn't exist
if not os.path.exists("cleaned"):
    os.makedirs("cleaned")

# Read all CSV files
orders = pd.read_csv("data/orders.csv")
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
order_items = pd.read_csv("data/order_items.csv")

# Store all issues found during cleaning
issues = []

# Function to clean orders data

def clean_orders():

    print("Cleaning Orders...")

    # Convert order_date into datetime format
    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce",
        dayfirst=True
    )

    # Count invalid dates
    invalid_dates = orders["order_date"].isnull().sum()
    issues.append(f"Invalid Dates Found : {invalid_dates}")

    # Replace missing customer IDs
    missing_customer = orders["customer_id"].isnull().sum()
    issues.append(f"Missing Customer IDs : {missing_customer}")

    orders["customer_id"] = orders["customer_id"].fillna("UNKNOWN")

    # Remove duplicate rows
    before = len(orders)

    orders.drop_duplicates(inplace=True)

    after = len(orders)

    issues.append(f"Duplicate Orders Removed : {before-after}")

    # Save cleaned file
    orders.to_csv("cleaned/orders_clean.csv", index=False)

    print("Orders cleaned successfully.\n")


# Function to clean products

def clean_products():

    print("Cleaning Products...")

    cleaned_names = []

    for name in products["product_name"]:

        name = str(name)

        # Remove extra spaces
        name = name.strip()

        # Convert to title case
        name = name.title()

        cleaned_names.append(name)

    products["product_name"] = cleaned_names

    products.to_csv("cleaned/products_clean.csv", index=False)

    print("Products cleaned successfully.\n")



# Function to validate customer emails

def validate_emails():

    print("Checking Emails...")

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    invalid_email_list = []

    for index, row in customers.iterrows():

        email = str(row["email"])

        if re.match(pattern, email) is None:

            invalid_email_list.append(row)

    invalid_df = pd.DataFrame(invalid_email_list)

    issues.append(f"Invalid Emails : {len(invalid_df)}")

    invalid_df.to_csv(
        "cleaned/invalid_emails.csv",
        index=False
    )

    print("Email validation completed.\n")


# Check referential integrity

def check_referential_integrity():

    print("Checking Order IDs...")

    valid_order_ids = set(orders["order_id"])

    invalid_rows = []

    for index, row in order_items.iterrows():

        if row["order_id"] not in valid_order_ids:

            invalid_rows.append(row)

    invalid_df = pd.DataFrame(invalid_rows)

    issues.append(
        f"Invalid Order References : {len(invalid_df)}"
    )

    invalid_df.to_csv(
        "cleaned/invalid_order_items.csv",
        index=False
    )

    print("Referential integrity checked.\n")


# Check negative quantity

def check_negative_quantity():

    count = 0

    for quantity in order_items["quantity"]:

        if quantity < 0:
            count += 1

    issues.append(f"Negative Quantity Rows : {count}")


# Check discount values

def check_discount():

    count = 0

    for discount in order_items["discount_percent"]:

        if discount > 100:
            count += 1

    issues.append(f"Discount Greater Than 100 : {count}")


# Save unchanged cleaned files

def save_other_files():

    customers.to_csv(
        "cleaned/customers_clean.csv",
        index=False
    )

    order_items.to_csv(
        "cleaned/order_items_clean.csv",
        index=False
    )


# Save issue report

def save_report():

    report = open("cleaned/issues_report.txt", "w")

    report.write("DATA CLEANING REPORT\n")
    report.write("----------------------------\n\n")

    for item in issues:
        report.write(item + "\n")

    report.close()



# Main Program

print("Starting Data Cleaning...\n")

clean_orders()

clean_products()

validate_emails()

check_referential_integrity()

check_negative_quantity()

check_discount()

save_other_files()

save_report()

print("Cleaning Completed Successfully.\n")

print("Summary Report\n")

for item in issues:
    print(item)