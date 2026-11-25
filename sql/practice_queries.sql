-- Beginner SQL practice using fictional order data.
-- Compatible with SQLite.

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer TEXT NOT NULL,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    city TEXT
);

INSERT OR REPLACE INTO orders
    (order_id, customer, product, quantity, unit_price, city)
VALUES
    (1, 'Asha', 'Notebook', 3, 45.00, 'Kolkata'),
    (2, 'Ravi', 'Pen', 10, 10.00, 'Delhi'),
    (3, 'Mina', 'Backpack', 1, 650.00, 'Kolkata'),
    (4, 'Kabir', 'Notebook', 5, 45.00, 'Pune'),
    (5, 'Asha', 'Pen', 4, 10.00, 'Kolkata');

-- 1. View all rows.
SELECT * FROM orders;

-- 2. Calculate revenue for each order.
SELECT
    order_id,
    product,
    quantity * unit_price AS revenue
FROM orders;

-- 3. Calculate revenue by product.
SELECT
    product,
    SUM(quantity * unit_price) AS total_revenue
FROM orders
GROUP BY product
ORDER BY total_revenue DESC;

-- 4. Filter orders with more than one item.
SELECT customer, product, quantity
FROM orders
WHERE quantity > 1;

-- 5. Count orders by city.
SELECT city, COUNT(*) AS order_count
FROM orders
GROUP BY city
ORDER BY order_count DESC;

-- 6. Calculate an overall summary.
SELECT
    COUNT(*) AS number_of_orders,
    SUM(quantity * unit_price) AS overall_revenue,
    AVG(quantity * unit_price) AS average_order_value
FROM orders;
