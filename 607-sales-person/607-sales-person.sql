# Write your MySQL query statement below
SELECT SalesPerson.name from SalesPerson
WHERE sales_id not in
(SELECT sales_id FROM Orders as o
left join company as c
on o.com_id = c.com_id 
WHERE c.name = 'RED');