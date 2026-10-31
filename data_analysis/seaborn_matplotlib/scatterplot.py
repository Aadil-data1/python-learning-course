import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv = Path(__file__).with_name("income.csv")
df = pd.read_csv(csv)
print(df.info())



plt.scatter(
    df["income"],
    df["purchase_amount"],
    alpha=0.6
)

plt.xlabel("income")
plt.ylabel("purchase amount")
plt.title("Income vs Purchase Amount")

plt.tight_layout()
plt.show()