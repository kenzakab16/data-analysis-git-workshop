import pandas as pd

df = pd.read_csv("data/sales.csv")
total_revenue = (df["quantity"] * df["price"]).sum()
print(f"Total Revenue: ${total_revenue}")
