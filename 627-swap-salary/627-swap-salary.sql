# Write your MySQL query statement below
UPDATE Salary
SET sex =
    CASE sex
        WHEN 'm' then 'f' ELSE 'm'
    END;


# sex = IF( sex = 'm', 'f', 'm');


# IF(condition, value_if_true, value_if_false)