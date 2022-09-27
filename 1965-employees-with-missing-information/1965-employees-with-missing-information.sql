# Write your MySQL query statement below


SELECT employee_id FROM
    (SELECT Employees.employee_id, name, salary FROM Employees 
    LEFT JOIN Salaries
    ON Employees.employee_id = Salaries.employee_id

    UNION

    SELECT Salaries.employee_id, name, salary FROM Salaries
    LEFT JOIN Employees
    ON Salaries.employee_id = Employees.employee_id)
AS T
WHERE name is NULL or salary is NULL
ORDER BY employee_id;


