# Retail Sales Analysis using PostgreSQL and Python

## Project Overview
This project analyzes retail sales data using PostgreSQL and Python to identify revenue trends, top-performing product categories, customer spending patterns, and regional sales performance.

## Objectives
- Analyze total revenue and units sold.
- Identify the best-performing product categories.
- Track monthly sales trends.
- Compare sales across regions.
- Identify top products and valuable customers.
- Visualize business insights using charts.

## Tools & Technologies
- PostgreSQL — Data storage and SQL analysis
- Python — Data analysis
- Pandas — Data manipulation
- Matplotlib — Data visualization
- VS Code — Development environment

## Project Structure
```text
retail-sales-analysis/
├── sales_analysis.py
├── queries.sql
├── sales_by_category.png
├── monthly_sales_trend.png
├── sales_by_region.png
└── README.md
```

## Visualizations

### 1. Sales by Category
![Sales by Category](sales_by_category.png)

### 2. Monthly Sales Trend
![Monthly Sales Trend](monthly_sales_trend.png)

### 3. Sales by Region
![Sales by Region](sales_by_region.png)

## Key Analysis
The project explores revenue by category, monthly sales performance, regional comparisons, top products by revenue, customer spending, and category-wise revenue contribution.

## How to Run
1. Create a PostgreSQL database named `retail_sales_db`.
2. Create the `retail_sales` table and insert the sample dataset.
3. Run the SQL queries from `queries.sql`.
4. Install the Python dependencies:

   `pip install pandas matplotlib psycopg2-binary`

5. Configure your PostgreSQL connection details in `sales_analysis.py`.
6. Run:

   `python sales_analysis.py`

## Note
This project uses sample retail sales data for learning and demonstration purposes.

## Author
Rahul Raigar