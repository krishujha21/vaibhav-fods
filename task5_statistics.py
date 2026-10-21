import pandas as pd

# Task 5
df = pd.read_csv("inventory_data.csv")

stock = df["Stock_Quantity"]
stats = {"Average": stock.mean(),
         "Minimum": stock.min(),
         "Maximum": stock.max(),
         "Std Dev": stock.std()}

print("Task 5: Stock quantity statistics\n")
for name in stats:
    print(f"{name:8}: {stats[name]:.2f}")