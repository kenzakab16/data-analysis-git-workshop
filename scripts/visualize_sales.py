import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv")
df.groupby("product")["quantity"].sum().plot(kind="bar")
plt.title("Total Quantity Sold per Product")
plt.show()
