SELECT manager_id, TO_CHAR(null) job_id, TO_NUMBER(null)department_id, SUM(salary)
FROM employees
GROUP BY manager_id
UNION 
SELECT TO_NUMBER(null), job_id, TO_NUMBER(null), SUM(salary)
FROM employees
GROUP BY job_id
UNION
SELECT TO_NUMBER(null), TO_CHAR(null), department_id, SUM(salary)
FROM employees
GROUP BY department_id;

SELECT department_id FROM employees
WHERE manager_id = 100
MINUS 
SELECT department_id FROM employees
WHERE manager_id IN (145, 201);


SELECT first_name, last_name, salary FROM employees
WHERE first_name like '_a%'
INTERSECT
SELECT first_name, last_name, salary FROM employees
WHERE UPPER(last_name) like '%S%'
ORDER BY salary DESC;

select * from locations;
select * from countries;
select * from regions;

SELECT location_id, postal_code, city From locations l
JOIN countries c ON (c.country_id=l.country_id)
WHERE country_name IN ('Germany', 'Italy')
UNION ALL
SELECT location_id, postal_code, city From locations 
WHERE postal_code like '%9%';

SELECT
    country_id id,
    country_name country,
    region_id region
FROM countries 
WHERE LENGTH(country_name) > 8
UNION
SELECT
    country_id,
    country_name,
    region_id
FROM countries 
WHERE region_id != (SELECT region_id from regions where region_name = 'Europe')
ORDER BY country DESC;

 