import pandas as pd

# Task 3
df = pd.read_csv("inventory_data.csv")

reorder = df.loc[df["Stock_Quantity"] < df["Reorder_Level"], :]

print("Task 3: Products below reorder level\n")
print("Number of products to reorder:", len(reorder))
print(reorder.loc[:, ["Product_ID", "Product_Name", "Supplier",
                      "Stock_Quantity", "Reorder_Level"]])
