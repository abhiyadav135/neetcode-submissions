-- Write your query below
ALTER TABLE employees  ADD  bonus INT;
UPDATE employees
SET bonus = 
    CASE 
        WHEN employee_id%2=1 AND name  NOT LIKE 'M%'  THEN salary
        ELSE 0 
    END    ;

SELECT employee_id,bonus from employees
ORDER BY employee_id ASC ;    