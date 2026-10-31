import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

orders_csv = Path(__file__).with_name("orders_.csv")
df= pd.read_csv(orders_csv)

numeric_columns = df.select_dtypes(
    include="number"
).columns.tolist()

categorical_columns = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

print("Numerical columns:", numeric_columns)
print("Categorical columns:", categorical_columns)

#print(df.info())

df[["customer id","age", "purchase amount"]] = df[["customer id", "age", "purchase amount"]].apply(pd.to_numeric, errors='coerce') # changing columns to appropriate datatypes
df["purchase date"] = pd.to_datetime(df["purchase date"], errors = "coerce")
#print(df.info())

print(df.isna().sum())

missing_percent = df.isna().mean() * 100
#print(missing_percent)

#print(df["city"].value_counts())      # to check how frequently each city occurs

ages = df.sort_values("age", ascending=False).head(10)     # to inspect top 10 oldest customers
#print(ages)

analyze = df.groupby("city")["purchase amount"].agg(       # calculating average, minimum, and maximum purchase amounts in each city?
    ["mean", "min", "max"]
)

#print(analyze)

city_avg = df.groupby("city")["purchase amount"].mean()   # calculates the average purchase amount for each city.
#print(city_avg)

below_25 = df["purchase amount"].quantile(0.25)  # calculates the value below which are 25% values of purchase amount
#print(below_25)


 # calculating pearson correlation, which measures the strength and direction of a linear relationship. it value lies between -1 and +1

correlation = df["age"].corr(df["purchase amount"])   # determine the linear relationship between age and purchase amount. 

#print(correlation)

plt.figure(figsize=(10,7))
sns.heatmap(
    correlation,
    annot= True,
    cmap= "coolwarm",
    vmin=1,
    vmax=1
)

plt.title("Correlation Heatmap")
plt.tight_layout
plt.show()