
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    database="retail_sales_db",
    user="postgres",
    password="123",
    port="5432"
)

# Load sales data
query = """
SELECT order_date, category, product_name,
       quantity, price, region,
       quantity * price AS revenue
FROM retail_sales;
"""

df = pd.read_sql_query(query, conn)
conn.close()

# 1. Sales by Category
category_sales = df.groupby("category")["revenue"].sum()
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# 2. Monthly Sales Trend
df["order_date"] = pd.to_datetime(df["order_date"])
monthly_sales = df.groupby(
    df["order_date"].dt.to_period("M")
)["revenue"].sum()

monthly_sales.index = monthly_sales.index.astype(str)
monthly_sales.plot(kind="line", marker="o",
                   title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# 3. Sales by Region
region_sales = df.groupby("region")["revenue"].sum()
region_sales.plot(kind="bar", title="Sales by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

print("All three graphs generated successfully!")
