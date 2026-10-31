import pandas as pd
from pathlib import Path

csv = Path(__file__).with_name("customers.csv")
customers = pd.read_csv(csv)

csv_2 = Path(__file__).with_name("orders_.csv")
orders = pd.read_csv(csv_2)

 # Attach customer Details to each other
combined = pd.merge(
    orders,
    customers,
    left_on= "customer id",
    right_on= "customer_id",
    how= "left"

)

#print("Combined Orders")
#print(combined)

# Calculate each customer's total spending.
customer_spending = (
    combined.groupby(
        ["customer id", "city"],
        dropna=False
    )["purchase amount"]
    .sum()
    .reset_index()
)

#print("\nCustomer spending summary:")
#print(customer_spending)

# Save the combined data and summary.
combined.to_csv(
    "combined_orders.csv",
    index=False
)