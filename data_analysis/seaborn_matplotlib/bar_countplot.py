import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

csv = Path(__file__).with_name("sales_data.csv")
df = pd.read_csv(csv)



city_sales = (
    df.groupby("city")["sales"]
    .sum()
    .sort_values(ascending=False)
)

city_sales.plot(kind="bar", figsize=(8, 5))

plt.xlabel("City")
plt.ylabel("Total sales")
plt.title("Total Sales by City")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# countplot() — How many observations belong to each category

df["city"].value_counts()

sns.countplot(data=df, x="city")

plt.title("Number of Records by City")
plt.xlabel("City")
plt.ylabel("Record count")

plt.tight_layout()
plt.show()


# violinplot
# #Wider sections indicate ranges where observations are more concentrated; narrower sections indicate ranges where they are less concentrated
sns.violinplot(  
    data=df,
    x="city",
    y="sales"
)

plt.title("Purchase Distribution by City")
plt.xlabel("City")
plt.ylabel("sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()