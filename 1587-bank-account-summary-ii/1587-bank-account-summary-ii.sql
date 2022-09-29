# Write your MySQL query statement below
SELECT name, sum(amount) as BALANCE
FROM users u
JOIN transactions t
ON u.account = t.account
GROUP BY u.account
having sum(amount) > 10000