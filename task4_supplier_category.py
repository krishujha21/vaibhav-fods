import pandas as pd

# Task 4
df = pd.read_csv("inventory_data.csv")
df["Inventory_Value"] = df["Stock_Quantity"] * df["Unit_Cost"]

summary = df.groupby(["Supplier", "Category"])[["Stock_Quantity", "Inventory_Value"]].sum()

print("Task 4: Supplier-Category summary\n")
print(summary)
