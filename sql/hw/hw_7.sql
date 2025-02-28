select * from regions;
select * from employees;
select * from departments;
select * from locations;
select * from jobs;
select * from job_history;
select * from countries;

select job_id, LENGTH(job_title) from jobs;
select * from employees where TO_CHAR(hire_date, 'YYYY') = '2005';
SELECT 
    region_name,
    COUNT(*)
FROM employees e 
JOIN departments d ON (e.department_id=d.department_id)
JOIN locations l ON (d.location_id=l.location_id)
JOIN countries c ON (l.country_id=c.country_id)
JOIN regions r ON (c.region_id=r.region_id)
GROUP BY region_name;


SELECT 
    first_name, 
    last_name, 
    e.department_id,
    department_name,
    job_id,
    street_address,
    country_name, 
    region_name
FROM employees e 
JOIN departments d ON (d.department_id=e.department_id)
JOIN locations l ON (d.location_id=l.location_id)
JOIN countries c ON (l.country_id=c.country_id)
JOIN regions r ON (c.region_id=r.region_id);


SELECT 
    emp2.first_name,
    COUNT(*)
FROM employees emp1 
JOIN employees emp2 ON (emp1.manager_id = emp2.employee_id)
GROUP BY  emp2.first_name
HAVING COUNT(*) > 6;

SELECT
    department_name, 
    COUNT(*)
FROM employees e 
JOIN departments d USING (department_id)
GROUP BY department_name
HAVING COUNT(*) > 30;


SELECT department_name
FROM employees e
RIGHT OUTER JOIN departments d ON (e.department_id=d.department_id)
WHERE first_name is null;

select * from employees;

SELECT * FROM employees emp1
JOIN employees emp2 ON (emp1.manager_id = emp2.employee_id)
WHERE emp1.hire_date < TO_DATE('01-JAN-2005', 'DD-MM-YYYY') 
AND TO_CHAR(emp2.hire_date, 'YYYY') = '2005';

select * from jobs;

SELECT
    country_name,
    r.region_name
FROM countries c
NATURAL JOIN regions r; 


SELECT
    first_name, 
    last_name, 
    salary
FROM employees e
JOIN jobs j ON (e.job_id=j.job_id AND salary < min_salary + 1000);



SELECT
    distinct NVL((first_name||' '||last_name), 'no employee') name,
    NVL(country_name, 'no country info') country
FROM employees e
LEFT OUTER JOIN departments d ON (e.department_id=d.department_id)
LEFT OUTER JOIN locations l ON (d.location_id=l.location_id)
FULL OUTER JOIN countries c ON (l.country_id=c.country_id);


SELECT
    first_name,
    last_name,
    country_name
FROM employees CROSS JOIN countries;    


SELECT 
    NVL(region_name, 'no region') region_name, 
    NVL(COUNT(*), 0) qty
FROM employees e, departments d, locations l, countries c, regions r
WHERE e.department_id(+)=d.department_id
AND d.location_id(+)=l.location_id
AND l.country_id(+)=c.country_id
AND c.region_id(+)=r.region_id
GROUP BY region_name;
    
SELECT 
    first_name, 
    last_name, 
    e.department_id,
    NVL(department_name, 'no department') department_name,
    job_id,
    street_address,
    country_name, 
    region_name
FROM employees e, departments d, locations l, countries c, regions r
WHERE d.department_id=e.department_id
AND d.location_id=l.location_id
AND l.country_id=c.country_id
AND c.region_id=r.region_id;
