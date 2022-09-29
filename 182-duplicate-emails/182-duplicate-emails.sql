# Write your MySQL query statement below
SELECT email
FROM Person
Group by email
Having COUNT(email) >1