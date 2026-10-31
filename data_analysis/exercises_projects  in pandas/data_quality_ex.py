import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104],         # Each customer ID in the customer table should be unique.
    "Name": ["Aadi", "Sara", "Rahul", "John"],
    "City": ["Delhi", "Mumbai", "Chennai", "Delhi"]
})

orders = pd.DataFrame({
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer_ID": [101, 102, 101, 105, 104],     # Customer 105 does not exist in the customer table.
    "Quantity": [2, 3, -1, 1, 4],                # one quantity is negative
    "Price": [500, 300, 400, 800, 250]
})

# Validate the customer table

assert customers["Customer_ID"].notna().all()   # checks whether every ID is present and asks whether every element is True.

if not customers["Customer_ID"].is_unique:
    raise ValueError("Duplicate customer IDs found.")

#print("Customer table validation passed.")

# Validate the order data

invalid_quantity = orders.loc[
    orders["Quantity"] < 0
]

print("Invalid quantities:")
#print(invalid_quantity)

# Merge safely

combined = orders.merge(
    customers,
    on="Customer_ID",
    how="left",
    validate="many_to_one",
    indicator=True
)
#print(combined)
#print(combined["_merge"].value_counts())

# Calculate sales

combined["Sales"] = (
    combined["Quantity"] * combined["Price"]
)

# Create a quality summary
quality_report = pd.DataFrame({
    "Missing": combined.isna().sum(),
    "Data_Type": combined.dtypes.astype(str)
})

#print(quality_report)

# . Check the row count

if len(combined) != len(orders):
    raise ValueError("Unexpected row-count change after merge.")

#print("Merge row-count validation passed.")

# Check the unmatched records separately

unmatched = combined.loc[
    combined["_merge"] == "left_only"
]

print(unmatched[
    ["Order_ID", "Customer_ID", "Sales"]
])

