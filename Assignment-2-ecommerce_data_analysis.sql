CREATE DATABASE ecommerce;

USE ecommerce; 

#creating 4 tables schema
#table1 - customers
CREATE TABLE customers(
customer_id INT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL, 
city VARCHAR(50) NOT NULL,
state VARCHAR(50) NOT NULL, 
join_date DATE NOT NULL,
is_premium BOOLEAN DEFAULT FALSE
);

-- Index for filtering by city/state
CREATE INDEX idx_customers_city ON customers(city);
CREATE INDEX idx_customers_state ON customers(state);

#table 2 - products
CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100) NOT NULL,
category VARCHAR(50) NOT NULL,
brand VARCHAR(50) NOT NULL,
unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price > 0),
stock_qty INT NOT NULL DEFAULT 0 CHECK (stock_qty >= 0)
);

-- Index for filtering by category
CREATE INDEX idx_products_category ON products(category);

#table 3 - orders
CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT NOT NULL,
order_date DATE NOT NULL,
status VARCHAR(20) NOT NULL DEFAULT 'Pending' CHECK (status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')),
total_amount DECIMAL(12, 2) NOT NULL CHECK (total_amount >= 0),

FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Index for date-based filtering and sorting
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_orders_status ON orders(status);

#table 4 - order_items
CREATE TABLE order_items (
item_id INT PRIMARY KEY,
order_id INT NOT NULL,
product_id INT NOT NULL,
quantity INT NOT NULL CHECK (quantity > 0),
unit_price DECIMAL(10,2) NOT NULL CHECK(unit_price > 0),
discount_pct DECIMAL(5,2) DEFAULT 0 CHECK (discount_pct BETWEEN 0 AND 100),

FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
);

#Data Loading 
-- INSERT: customers

INSERT INTO customers VALUES 
(101, 'Aarav',  'Sharma', 'aarav.s@email.com',  'Mumbai',    'Maharashtra', '2024-01-15', TRUE), 
(102, 'Priya',  'Patel',  'priya.p@email.com',  'Ahmedabad', 'Gujarat',     '2024-02-20', FALSE), 
(103, 'Rohan',  'Gupta',  'rohan.g@email.com',  'Delhi',     'Delhi',       '2024-03-10', TRUE), 
(104, 'Sneha',  'Reddy',  'sneha.r@email.com',  'Hyderabad', 'Telangana',   '2024-04-05', FALSE), 
(105, 'Vikram', 'Singh',  'vikram.s@email.com', 'Jaipur',    'Rajasthan',   '2024-05-12', TRUE), 
(106, 'Ananya', 'Iyer',   'ananya.i@email.com', 'Chennai',   'Tamil Nadu',  '2024-06-18', FALSE), 
(107, 'Karan',  'Mehta',  'karan.m@email.com',  'Pune',      'Maharashtra', '2024-07-22', TRUE), 
(108, 'Divya',  'Nair',   'divya.n@email.com',  'Kochi',     'Kerala',      '2024-08-30', FALSE);

-- INSERT: products
INSERT INTO products VALUES 
(201, 'Wireless Earbuds',     'Electronics', 'BoAt',          1499.00, 250), 
(202, 'Cotton T-Shirt',       'Clothing',    'Levis',         799.00,  500), 
(203, 'Smart Watch',          'Electronics', 'Noise',         2999.00, 150), 
(204, 'Running Shoes',        'Clothing',    'Nike',          4599.00, 120), 
(205, 'Bluetooth Speaker',    'Electronics', 'JBL',           3499.00, 200), 
(206, 'Bedsheet Set',         'Home',        'Spaces',        1299.00, 300), 
(207, 'Laptop Stand',         'Electronics', 'AmazonBasics',  899.00,  180), 
(208, 'Cushion Covers (Set)', 'Home',        'HomeCenter',    599.00,  400);

-- INSERT: orders
INSERT INTO orders VALUES 
(1001, 101, '2024-08-01', 'Delivered',  4498.00), 
(1002, 102, '2024-08-03', 'Delivered',  799.00), 
(1003, 103, '2024-08-05', 'Shipped',    7498.00), 
(1004, 101, '2024-08-10', 'Delivered',  3499.00), 
(1005, 104, '2024-08-12', 'Cancelled',  2999.00), 
(1006, 105, '2024-08-15', 'Delivered',  5898.00), 
(1007, 106, '2024-08-18', 'Pending',    1299.00), 
(1008, 103, '2024-08-20', 'Delivered',  899.00), 
(1009, 107, '2024-08-25', 'Shipped',    6098.00), 
(1010, 108, '2024-08-28', 'Delivered',  1598.00);

-- INSERT: order_items
INSERT INTO order_items VALUES 
(5001, 1001, 201, 2, 1499.00, 0), 
(5002, 1001, 207, 1, 899.00,  10), 
(5003, 1002, 202, 1, 799.00,  0), 
(5004, 1003, 203, 1, 2999.00, 0), 
(5005, 1003, 204, 1, 4599.00, 5), 
(5006, 1004, 205, 1, 3499.00, 0), 
(5007, 1005, 203, 1, 2999.00, 0), 
(5008, 1006, 201, 1, 1499.00, 10), 
(5009, 1006, 204, 1, 4599.00, 5), 
(5010, 1007, 206, 1, 1299.00, 0), 
(5011, 1008, 207, 1, 899.00,  0), 
(5012, 1009, 205, 1, 3499.00, 0), 
(5013, 1009, 208, 2, 599.00,  15), 
(5014, 1010, 206, 1, 1299.00, 0), 
(5015, 1010, 208, 1, 599.00,  0);

# SECTION A

#Q.1
SELECT * FROM customers;

#Q.2
SELECT first_name, last_name, city FROM customers;

DESCRIBE customers; #schema

#Q.3
SELECT DISTINCT category
FROM products;

#Q.4
DESCRIBE customers; -- Primary key - customer_id
DESCRIBE products; -- Primary Key - product_id
DESCRIBE orders; -- Primary Key - order_id
DESCRIBE order_items; -- Primary Key - item_id

/* Primary Key is unique identifier for a specific row in a datebase table. It ensures
each record is distinguishable, prevents duplicate data and acts as a the target for foreign key
when linking different tables together. */ 

#Q.5
DESCRIBE customers; -- Constraint on eamil - unique, not null
INSERT INTO customers VALUE (109, 'divya', 'sharma', 'divya.n@email.com', 'Jaipur', 'Rajasthan', '2025-12-2', FALSE);
-- Error on duplicate email entry because of constraint (unique)

#Q.6
DESCRIBE products;
INSERT INTO products VALUE (209, 'Analog watch' , 'Clothing' ,'Titan', -50.00, 100);
-- Gives Error, Constraint CHECK is violated 
--  the constraint make sure that the unit_price is greater than 0

#SECTION - B 

#Q.7
SELECT status, order_id FROM orders
WHERE status = 'Delivered';

#Q.8
SELECT category, product_id, product_name FROM products
WHERE unit_price > 2000.00

#Q.9
SELECT first_name, last_name FROM customers
WHERE ((join_date >= '2024-01-01' AND join_date <= '2024-12-31') AND (state = 'Maharashtra'))

#Q.10
SELECT order_id FROM orders
WHERE (order_date >= '2024-08-10' AND order_date <= '2024-08-25') AND ( status != 'Cancelled')

#Q.11
/*idx_orders_date is an index created on the order_date column of the orders table.
The index stores the order_date values in a sorted structure so MySQL can quickly locate rows for a specific date or date range.
*/
SELECT order_id FROM orders
WHERE order_date = '2025-05-01';

#Q.12
SELECT * FROM customers 
WHERE YEAR(join_date) = 2024;

/* No, the index on join_date would usually not be used efficiently in this query */
/* Index friendly query*/
SELECT * FROM customers
WHERE join_date >= '2024-01-01' AND join_date < '2025-01-01';

# SECTION -C

#Q.13
SELECT COUNT(order_id) AS total_orders FROM orders;

#Q.14
SELECT SUM(total_amount) AS total_revenue  FROM orders
WHERE status = 'Delivered';

#Q.15
SELECT category, AVG(unit_price) AS average_unit_price 
FROM products
GROUP BY category;

#Q.16
SELECT status, COUNT(order_id) AS total_orders, SUM(total_amount) AS total_revenue
FROM orders
GROUP BY status
ORDER BY total_revenue DESC;

#Q.17
SELECT category, MAX(unit_price), MIN(unit_price) FROM products
GROUP BY category;

#Q.18
SELECT category, AVG(unit_price) AS avg_unit_price FROM products
GROUP BY category
HAVING avg_unit_price > 2000.0;

# SECTION - D

#Q.19
SELECT order_id, order_date, first_name, last_name, total_amount
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;

#Q.20
SELECT c.customer_id, c.first_name, c.last_name, o.order_id
FROM customers AS c
LEFT JOIN orders AS o
On c.customer_id = o.customer_id;

#Q.21
SELECT
    o.order_id,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.discount_pct
FROM orders AS o
INNER JOIN order_items AS oi
ON o.order_id = oi.order_id
INNER JOIN products AS p
ON oi.product_id = p.product_id
ORDER BY o.order_id, p.product_name;


#Q.22

/* LEFT JOIN
A LEFT JOIN returns:
All rows from the left table
Matching rows from the right table
NULL for right-table columns when no match exists

Ex: SELECT c.customer_id, c.first_name, c.last_name, o.order_id
FROM customers AS c
LEFT JOIN orders AS o
On c.customer_id = o.customer_id;

RIGHT JOIN: 
A RIGHT JOIN returns:
All rows from the right table
Matching rows from the left table
NULL for left-table columns when no match exists

Ex :SELECT
    c.customer_name,
    o.order_id
    FROM customers c
    RIGHT JOIN orders o
    ON c.customer_id = o.customer_id;
    
FULL JOIN:
A FULL OUTER JOIN returns:
All matching rows
All unmatched rows from the left table
All unmatched rows from the right table
 */
 
 #Q.23
 INSERT INTO orders
(order_id, customer_id, order_date, status, total_amount)
VALUES
(1012, 999, CURDATE(), 'Pending', 1500.00);
/*The database will reject the insert because it violates the foreign key constraint.*/
 
 #SECTION -E
 
 #Q.24
 SELECT product_id, product_name, unit_price,
 CASE
 WHEN unit_price < 1000 THEN 'Budget'
 WHEN unit_price > 1000 AND unit_price < 3000 THEN 'Mid-Range'
 WHEN unit_price > 3000 THEN 'Premium'
 END AS price_tier
 FROM products
 ORDER BY unit_price;
 
 #Q.25
 SELECT
    SUM(CASE
            WHEN status = 'Delivered' THEN 1
            ELSE 0
        END) AS delivered_orders,
    SUM(CASE
            WHEN status = 'Shipped' THEN 1
            ELSE 0
        END) AS shipped_orders,
	SUM(CASE
            WHEN status = 'Cancelled' THEN 1
            ELSE 0
        END) AS cancelled_orders,
	SUM(CASE 
        WHEN status = 'Pending' THEN 1
        ELSE 0
        END) AS pending_orders
FROM orders;
 
 
#Q.26

/* 
A - Atomicity
A transaction is treated as a single unit of work. Either all operations succeed, or none of them do.

Bank Transfer Ex:
A transfer involves two steps:
1.Deduct ₹5,000 from Account A
2.Add ₹5,000 to Account B

Suppose the money is deducted from A, but the system crashes before adding it to B.

Without Atomicity:

- Account A loses ₹5,000
- Account B receives nothing
- Money effectively disappears

With Atomicity:

- Either both steps complete, or both are rolled back.
- The database returns to its previous state if any part fails.

C - Consistency
A transaction must move the database from one valid state to another valid state, preserving all rules and constraints.

Bank Transfer Example: 
Before transfer:

- Account A = ₹10,000
- Account B = ₹15,000
- Total = ₹25,000

After transferring ₹5,000:

- Account A = ₹5,000
- Account B = ₹20,000
- Total = ₹25,000

The total amount of money remains unchanged.

Without Consistency:

A bug might deduct ₹5,000 but add ₹6,000.
Total money becomes ₹26,000.
Business rules are violated.

I - Isolation
Multiple transactions running at the same time should not interfere with one another.

Bank Transfer Example: 
Assume Account A has ₹10,000.

Two transactions start simultaneously:

- Transaction T1 withdraws ₹4,000.
- Transaction T2 withdraws ₹7,000.

Without Isolation:

- Both transactions may read the same initial balance (₹10,000).
- Both may proceed.
- Final balance could become incorrect.

With Isolation:

- The database controls concurrent access.
- Transactions behave as if they ran one after another.

D - Durability
Once a transaction is committed, its changes are permanently saved, even if the system crashes immediately afterward.

Bank Transfer Example: 
A transfer completes successfully:

- ₹5,000 deducted from A
- ₹5,000 added to B
- Transaction committed

Immediately after commit, the server loses power.

Without Durability:

- The transfer may disappear after restart.
- Users see old balances.

With Durability:

- The committed transaction is recovered from logs/storage.
- Balances remain correct.

 */
 
 #Q.27
START TRANSACTION;

-- 1. Insert the order
INSERT INTO orders
    (order_id, customer_id, order_date, status, total_amount)
VALUES
    (1011, 102, CURDATE(), 'Pending', 1598.00);

-- 2. Insert two order items
INSERT INTO order_items
    (order_id, product_id, quantity, unit_price, discount_pct)
VALUES
    (1011, 201, 2, 499.00, 0);

INSERT INTO order_items
    (order_id, product_id, quantity, unit_price, discount_pct)
VALUES
    (1011, 305, 1, 600.00, 0);

-- 3. Update stock quantities
UPDATE products
SET stock_qty = stock_qty - 2
WHERE product_id = 201;

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 305;

COMMIT;
 