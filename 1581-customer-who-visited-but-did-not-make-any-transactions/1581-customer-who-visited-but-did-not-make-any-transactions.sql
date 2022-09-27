# Write your MySQL query statement below
# select customer_id, count(distinct(visit_id))
select customer_id, count(customer_id) as count_no_trans
FROM Visits as v
left join Transactions as T
on v.visit_id = t.visit_id
Where transaction_id is NULL
GROUP BY customer_id