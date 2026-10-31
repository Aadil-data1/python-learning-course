import pandas as pd
from pathlib import Path

sales_data = Path(__file__).with_name("sales_data.csv")
df =pd.read_csv(sales_data)

#print(df["sales"].dtype)   

#print(df.head())
#print(df.columns)

aggregate = df.groupby("city")["sales"].agg(
    ["sum", "mean", "min", "max"]
)

#print(aggregate)

total = df.pivot_table(           # calculating total sales of each product in different cities
    index="city",
    columns="product",
    values="sales",
    aggfunc="sum",
    fill_value=0,
    margins= True
)

print(total)


nr_of_transc  = df.pivot_table(
    index="city",
    columns="product",                   # calculating number of transctions occured for each product
    values="sales",
    aggfunc="count",
    fill_value=0
)

print(nr_of_transc)