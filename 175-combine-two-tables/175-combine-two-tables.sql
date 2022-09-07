# Write your MySQL query statement below
SELECT firstName, lastName, city, state FROM Person
LEFT JOIN Address
ON PERSON.personId = Address.personId