import sqlite3
import pandas as pd

conn = sqlite3.connect("../ecommerce.db")

query1 = """
SELECT
    p.category,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS total_revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
WHERE oi.quantity > 0
GROUP BY p.category
ORDER BY total_revenue DESC;
"""

query2 = """ SELECT
    o.customer_id,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_percent / 100.0)
        ),
        2
    ) AS total_order_value
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
WHERE oi.quantity > 0
GROUP BY o.customer_id
ORDER BY total_order_value DESC
LIMIT 10;"""

query3 = """ SELECT
    strftime('%Y-%m', order_date) AS month,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;"""

query4 = """ SELECT DISTINCT
    customer_id
FROM orders
WHERE customer_id NOT IN
(
    SELECT customer_id
    FROM orders
    WHERE status='DELIVERED'
);"""

query5 = """ SELECT
    p.product_name,

    SUM(
        CASE
        WHEN oi.quantity > 0 THEN oi.quantity
        ELSE 0
        END
    ) AS purchased,

    ABS(
        SUM(
            CASE
            WHEN oi.quantity < 0 THEN oi.quantity
            ELSE 0
            END
        )
    ) AS returned

FROM order_items oi

JOIN products p
ON oi.product_id=p.product_id

GROUP BY p.product_name

HAVING returned > purchased;"""

query6 = """ SELECT

p.category,

ROUND(

100.0 *

SUM(
CASE
WHEN oi.quantity<0 THEN ABS(oi.quantity)
ELSE 0
END
)

/

SUM(ABS(oi.quantity))

,2)

AS return_rate

FROM order_items oi

JOIN products p

ON oi.product_id=p.product_id

GROUP BY p.category;"""

query7 = """ SELECT

o.region_code,

DATE(o.order_date) AS order_day,

ROUND(

SUM(

oi.quantity*oi.unit_price*

(1-oi.discount_percent/100.0)

)

,2)

AS daily_revenue,

ROUND(

SUM(

SUM(

oi.quantity*oi.unit_price*

(1-oi.discount_percent/100.0)

)

)

OVER(

PARTITION BY o.region_code

ORDER BY DATE(o.order_date)

)

,2)

AS running_total

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

WHERE oi.quantity>0

GROUP BY

o.region_code,

DATE(o.order_date);"""

query8 = """ SELECT

category,

product_name,

revenue,

DENSE_RANK()

OVER(

PARTITION BY category

ORDER BY revenue DESC

)

AS rank_in_category

FROM

(

SELECT

p.category,

p.product_name,

SUM(

oi.quantity*oi.unit_price*

(1-oi.discount_percent/100)

)

AS revenue

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

WHERE oi.quantity>0

GROUP BY

p.category,

p.product_name

);"""

query9 = """ SELECT

customer_id,

order_date,

LAG(order_date)

OVER(

PARTITION BY customer_id

ORDER BY order_date

)

AS previous_order,

JULIANDAY(order_date)

-

JULIANDAY(

LAG(order_date)

OVER(

PARTITION BY customer_id

ORDER BY order_date

)

)

AS days_gap

FROM orders;"""

query10 = """ WITH monthly_revenue AS (

    SELECT
        o.customer_id,
        strftime('%Y-%m', o.order_date) AS month,
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_percent / 100.0)
        ) AS revenue

    FROM orders o

    JOIN order_items oi
    ON o.order_id = oi.order_id

    WHERE oi.quantity > 0

    GROUP BY
        o.customer_id,
        month
)

SELECT

customer_id,

month,

ROUND(revenue,2) AS revenue,

CASE

WHEN revenue > 10000 THEN 'High'

WHEN revenue BETWEEN 5000 AND 10000 THEN 'Medium'

ELSE 'Low'

END AS customer_category

FROM monthly_revenue

ORDER BY month,revenue DESC;"""

query11 = """ WITH yearly AS (

SELECT

strftime('%Y',order_date) AS year,

strftime('%m',order_date) AS month,

SUM(

oi.quantity*oi.unit_price*

(1-oi.discount_percent/100)

)

AS revenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

WHERE oi.quantity>0

GROUP BY year,month

)

SELECT

year,

month,

ROUND(revenue,2),

ROUND(

LAG(revenue)

OVER(

PARTITION BY month

ORDER BY year

)

,2)

AS previous_year_revenue,

ROUND(

(

revenue-

LAG(revenue)

OVER(

PARTITION BY month

ORDER BY year

)

)

/

LAG(revenue)

OVER(

PARTITION BY month

ORDER BY year

)

*100

,2)

AS yoy_growth_percent

FROM yearly;"""

query12 = """ WITH purchases AS (

SELECT

o.customer_id,

o.order_date,

p.category

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

JOIN products p

ON oi.product_id=p.product_id

)

SELECT DISTINCT

customer_id,

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date

)

AS first_category,

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date DESC

)

AS latest_category,

CASE

WHEN

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date

)

=

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date DESC

)

THEN 'No'

ELSE 'Yes'

END AS category_shift

FROM purchases;"""

query13 = """ WITH purchases AS (

SELECT

o.customer_id,

o.order_date,

p.category

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

JOIN products p

ON oi.product_id=p.product_id

)

SELECT DISTINCT

customer_id,

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date

)

AS first_category,

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date DESC

)

AS latest_category,

CASE

WHEN

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date

)

=

FIRST_VALUE(category)

OVER(

PARTITION BY customer_id

ORDER BY order_date DESC

)

THEN 'No'

ELSE 'Yes'

END AS category_shift

FROM purchases;"""

query14 = """ WITH customer_revenue AS (

SELECT

o.customer_id,

SUM(

oi.quantity*oi.unit_price*

(1-oi.discount_percent/100)

)

AS revenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

WHERE oi.quantity>0

GROUP BY o.customer_id

)

SELECT

customer_id,

ROUND(revenue,2),

ROUND(

SUM(revenue)

OVER(

ORDER BY revenue DESC

)

,2)

AS cumulative_revenue,

ROUND(

100.0*

SUM(revenue)

OVER(

ORDER BY revenue DESC

)

/

SUM(revenue)

OVER()

,2)

AS cumulative_percent

FROM customer_revenue;"""

query15 = """WITH customer_orders AS (

SELECT

c.customer_id,

strftime('%Y-%m',c.registration_date) AS cohort,

strftime('%Y-%m',o.order_date) AS order_month

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

)

SELECT

cohort,

order_month,

COUNT(DISTINCT customer_id) AS customers

FROM customer_orders

GROUP BY

cohort,

order_month

ORDER BY

cohort,

order_month; """

result = pd.read_sql_query(query15, conn)

print(result)

conn.close()