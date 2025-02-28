SELECT 
    department_id, 
    COUNT(*) count, 
    MIN(salary) min_salary,
    MAX(salary) max_salary, 
    MIN(hire_date) min_hire_date, 
    MAX(hire_date) max_hire_date
FROM employees 
GROUP BY department_id
ORDER BY COUNT(*) DESC;

SELECT 
    SUBSTR(first_name, 1,1) first_letter,
    COUNT(*) name_count
FROM employees
GROUP BY SUBSTR(first_name, 1,1)
HAVING COUNT(*) > 1
ORDER BY name_count DESC;

SELECT 
    department_id, 
    salary, 
    COUNT(*)
FROM employees
GROUP BY department_id, salary;


SELECT 
    TO_CHAR(hire_date, 'DAY') day, 
    COUNT(*)
FROM employees
GROUP BY TO_CHAR(hire_date, 'DAY');


SELECT 
    department_id, 
    COUNT(*), 
    SUM(salary)
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 30 AND SUM(salary) > 300000;


select * from employees;

SELECT
    region_id, 
    SUM(LENGTH(country_name)) letter_qty
FROM countries
GROUP BY region_id
HAVING SUM(LENGTH(country_name)) > 50;


SELECT 
    job_id, 
    ROUND(AVG(salary)) avg_salary
FROM employees    
GROUP BY job_id;

SELECT 
    department_id,
    COUNT(DISTINCT job_id)    
FROM employees
GROUP BY department_id
HAVING COUNT(DISTINCT job_id) > 1;


SELECT
    department_id,
    job_id,
    MAX(salary),
    MIN(salary),
    ROUND(AVG(salary)) 
FROM employees
GROUP BY department_id, job_id 
HAVING AVG(salary) > 10000
ORDER BY department_id;

select first_name, manager_id, salary, commission_pct from employees where commission_pct is not null;

SELECT 
    manager_id,
    ROUND(AVG(salary))as average_salary
FROM employees
WHERE commission_pct is not null
GROUP BY manager_id
HAVING AVG(salary) BETWEEN 6000 AND 9000 
ORDER BY manager_id;


SELECT
    MAX(ROUND(AVG(salary), -3))
FROM employees
GROUP BY department_id;
    
