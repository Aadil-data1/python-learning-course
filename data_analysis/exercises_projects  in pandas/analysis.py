import os
import pandas as pd
from pathlib import Path



csv_path = Path(__file__).with_name("customers.csv")

df = pd.read_csv(csv_path)

# What does my data look like?
# How big is it?
# What columns exist?
# What types are they?
# What are the basic statistics?

print(df.head())                 
print(df.shape)
print(df.columns)
print(df.info())

print(df.iloc[1:3])  # Give me the data at this numerical position. simple understndin is "df.iloc[row_selection, column_selection]""

print(df.loc[:,["customer_id", "name"]])  # Give me the data with this label.

active_cust = df[df["is_active"]==True]  #  FIltering: checking for active customers
print(active_cust)


df["signup_date"] = pd.to_datetime(df["signup_date"], errors= "coerce")


print(df.sort_values("signup_date", ascending= True))  # sorting customers on the basis of sign up: from early to later

year = df["signup_date"].dt.year         # extracting year from signup_date column
print(year)

cntry_cust = df.groupby("country").size()  #  total number of customers from each country, calculates all rows
print(cntry_cust)

 # calculating customers from which countries will spend most with the business over their whole relationship with it.

agg_cust = df.groupby("country").agg(      
    lowest_spending = ("lifetime_value", "min"),
    highest_spending = ("lifetime_value", "max"), 
    average_spending  = ("lifetime_value", "mean")                                                                                                                                       #... relationship with it. lowest, highest and average
)
print(agg_cust)

