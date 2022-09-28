# Write your MySQL query statement below
SELECT ifnull(
(SELECT DISTINCT(salary)
FROM Employee
ORDER BY salary DESC
LIMIT 1
OFFSET 1), null) as SecondHighestSalary