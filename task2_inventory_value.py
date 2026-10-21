import pandas as pd

# Task 2
df = pd.read_csv("inventory_data.csv")

df["Inventory_Value"] = df["Stock_Quantity"] * df["Unit_Cost"]

print("Task 2: Inventory valuation table\n")
print(df.loc[0:14, ["Product_ID", "Product_Name", "Stock_Quantity",
                    "Unit_Cost", "Inventory_Value"]])
