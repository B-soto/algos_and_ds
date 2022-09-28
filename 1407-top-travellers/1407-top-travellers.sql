# Write your MySQL query statement below
SELECT name, 
(CASE WHEN SUM(distance) > 0 then SUM(distance) else 0 END )  as travelled_distance
FROM Users u
LEFT JOIN Rides r
on u.id = r.user_id
GROUP BY user_id
ORDER BY travelled_distance DESC, name