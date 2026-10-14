
-- 1. Overall Sales Summary
SELECT
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_units_sold,
    SUM(quantity * price) AS total_revenue,
    ROUND(AVG(quantity * price), 2) AS avg_order_value
FROM retail_sales;

-- 2. Sales by Category
SELECT
    category,
    SUM(quantity * price) AS total_sales
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Monthly Sales Trend
SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS sales_month,
    SUM(quantity * price) AS monthly_sales
FROM retail_sales
GROUP BY TO_CHAR(order_date, 'YYYY-MM')
ORDER BY sales_month;

-- 4. Sales by Region
SELECT
    region,
    SUM(quantity * price) AS total_sales
FROM retail_sales
GROUP BY region
ORDER BY total_sales DESC;

-- 5. Top 5 Products
SELECT
    product_name,
    SUM(quantity) AS units_sold,
    SUM(quantity * price) AS revenue
FROM retail_sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 5;

-- 6. Customer Spending
SELECT
    customer_name,
    COUNT(*) AS total_orders,
    SUM(quantity * price) AS total_spent
FROM retail_sales
GROUP BY customer_name
ORDER BY total_spent DESC;

-- 7. Category Revenue Contribution
SELECT
    category,
    ROUND(
        SUM(quantity * price) * 100.0 /
        SUM(SUM(quantity * price)) OVER (),
        2
    ) AS sales_percentage
FROM retail_sales
GROUP BY category
ORDER BY sales_percentage DESC;
