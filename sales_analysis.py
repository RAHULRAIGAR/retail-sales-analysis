
import os
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "127.0.0.1"),
    database=os.getenv("DB_NAME", "retail_sales_db"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.environ["DB_PASSWORD"],
    port=os.getenv("DB_PORT", "5432")
)

query = """
SELECT
    order_date,
    category,
    product_name,
    quantity,
    price,
    region,
    quantity * price AS revenue
FROM retail_sales;
"""

try:
    df = pd.read_sql_query(query, conn)
finally:
    conn.close()

if df.empty:
    raise ValueError("No sales records found in retail_sales.")

df["order_date"] = pd.to_datetime(df["order_date"])
df["revenue"] = pd.to_numeric(df["revenue"])

plt.style.use("ggplot")


def save_bar_chart(data, title, xlabel, filename):
    ax = data.plot(kind="bar", figsize=(9, 5), color="steelblue")
    ax.set_title(title, fontsize=15, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Revenue")
    ax.grid(axis="y", alpha=0.3)
    ax.tick_params(axis="x", rotation=30)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()


# 1. Sales by Category
category_sales = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
save_bar_chart(
    category_sales,
    "Retail Revenue by Category",
    "Product Category",
    "sales_by_category.png"
)

# 2. Monthly Sales Trend
monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
    .sum()
)
monthly_sales.index = monthly_sales.index.astype(str)

ax = monthly_sales.plot(
    kind="line", marker="o", figsize=(10, 5),
    color="darkgreen", linewidth=2
)
ax.set_title("Monthly Retail Sales Trend", fontsize=15, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.close()

# 3. Sales by Region
region_sales = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
save_bar_chart(
    region_sales,
    "Retail Revenue by Region",
    "Region",
    "sales_by_region.png"
)

print("All three charts generated successfully!")
