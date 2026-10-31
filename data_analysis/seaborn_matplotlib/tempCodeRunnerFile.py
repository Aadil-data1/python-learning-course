import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv = Path(__file__).with_name("sales_data.csv")
df = pd.read_csv(csv)

print(df.info())