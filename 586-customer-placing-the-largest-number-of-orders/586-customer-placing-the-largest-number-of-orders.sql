# Write your MySQL query statement below

with cte as
(SELECT customer_number, COUNT(order_number) as order_count
FROM Orders
group by customer_number)

SELECT customer_number
FROM cte
ORDER by order_count DESC
LIMIT 1


