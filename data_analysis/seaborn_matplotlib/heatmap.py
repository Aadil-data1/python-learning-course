import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

csv = Path(__file__).with_name("income.csv")

df = pd.read_csv(csv)

correlation_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,           # writes the numerical correlation inside each cell
    cmap="coolwarm",
    vmin=-1,               # vmin=-1 and vmax=1 keep the scale aligned with the full possible range of Pearson correlation...
    vmax=1                  # ...That makes the chart easier to interpret consistently.
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()