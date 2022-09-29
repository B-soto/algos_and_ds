# Write your MySQL query statement below
SELECT user_id, max(time_stamp) as last_stamp
FROM Logins
WHERE time_stamp BETWEEN '2020-01-00' AND '2021-01-00'
GROUP BY user_id



