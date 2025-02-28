SELECT * 
FROM employees
WHERE LENGTH(first_name) = 
(SELECT MAX(LENGTH(first_name)) from employees);

SELECT * 
FROM employees
WHERE salary > 
(SELECT AVG(salary) from employees);

SELECT city
FROM locations l
JOIN departments d ON (l.location_id=d.location_id)
JOIN employees e ON (e.department_id=d.department_id)
GROUP BY city
HAVING SUM(salary) = 
    (SELECT MIN(SUM(salary)) 
        FROM employees e1
            JOIN departments d1 ON (e1.department_id=d1.department_id)
            JOIN locations l1 ON (l1.location_id=d1.location_id)
    GROUP BY city);


SELECT * 
FROM employees 
WHERE manager_id IN (
    SELECT employee_id 
    FROM employees 
    WHERE salary > 15000
);

SELECT * FROM departments
WHERE department_id NOT IN
(SELECT department_id from employees 
WHERE department_id IS NOT NULL);


SELECT * 
FROM employees
WHERE job_id NOT IN
(SELECT job_id from jobs
where UPPER(job_title) like '%MANAGER%');

SELECT * FROM employees
WHERE employee_id IN 
(SELECT manager_id from employees
GROUP BY manager_id
HAVING COUNT(*) > 6); 

SELECT * FROM employees
WHERE department_id = 
(SELECT department_id FROM departments
WHERE department_name = 'IT');

SELECT * FROM employees
WHERE hire_date < TO_DATE('01-JAN-2005', 'DD-MON-YYYY') 
AND manager_id IN
(SELECT employee_id FROM employees
WHERE TO_CHAR(hire_date,'YYYY') = '2005'); 

SELECT * FROM employees
WHERE job_id IN
(SELECT job_id FROM jobs
WHERE LENGTH(job_title) > 15)
AND manager_id IN
(SELECT employee_id FROM employees
WHERE TO_CHAR(hire_date, 'MON') = 'JAN');