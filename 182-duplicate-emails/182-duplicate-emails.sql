# Write your MySQL query statement below
SELECT email FROM person
group by email
having COUNT(DISTINCT(id)) > 1