import pandas as pd

# Task 1
df = pd.read_csv("inventory_data.csv")

print("Task 1: First and last five records\n")
print("First five records:")
print(df.iloc[0:5])
print("\nLast five records:")
print(df.iloc[-5:])
print("\nTotal records:", len(df))
