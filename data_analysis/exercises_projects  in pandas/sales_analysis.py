import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv = Path(__file__).with_name("orders_with_sales.csv")

df = pd.read_csv(csv)


#print(df.info())

# Convert dates and identify invalid values.
df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

#print("Invalid or missing dates:", df["order_date"].isna().sum())

# Extract year and month.
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["yearmonth"] = df["order_date"].dt.to_period("M")

# Calculate monthly sales.
monthly_sales = (
    df.groupby("yearmonth")["sales"]
    .sum()
)

#print("\nMonthly sales:")
#print(monthly_sales)

# Plot the trend.
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()