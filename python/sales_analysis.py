import pandas as pd

# Load dataset
data = pd.read_csv("../data/sales.csv")

# Display basic info
print("Dataset Info:")
print(data.info())

# Total sales
total_sales = data["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by category
sales_by_category = data.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(sales_by_category)

# Profit by region
profit_by_region = data.groupby("Region")["Profit"].sum()
print("\nProfit by Region:")
print(profit_by_region)

# Top 10 products by sales
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:")
print(top_products)

# Save summary report
summary = data.groupby("Category")[["Sales", "Profit"]].sum()
summary.to_csv("../data/summary_report.csv")

print("\nSummary report saved successfully.")
