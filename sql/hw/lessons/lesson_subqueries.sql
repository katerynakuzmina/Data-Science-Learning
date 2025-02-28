select first_name, last_name, salary 
from employees where salary > (select AVG(salary) from employees);

select 
(select MIN(min_salary) from jobs) min_salary, 
(select MAX(LENGTH(first_name)) from employees) long_name
FROM dual;

select first_name, last_name from employees where
employee_id IN (select manager_id from employees);

select department_name, min(salary), max(salary) from
(select salary, department_name from employees e JOIN departments d
ON (e.department_id=d.department_id))
GROUP BY department_name;

SELECT first_name, last_name, salary
FROM employees
WHERE salary <
(SELECT MAX(salary)/5 FROM employees);

SELECT first_name, last_name, salary
FROM employees
WHERE salary >
(SELECT avg(salary) FROM employees);

SELECT first_name, last_name, salary
FROM employees
WHERE salary >=
(SELECT salary FROM employees WHERE employee_id=180);

select job_title from jobs j JOIN employees e ON(j.job_id=e.job_id)
group by job_title
having avg(salary) =
(select max(avg(salary)) from employees group by job_id);

SELECT first_name, last_name, salary from employees
where job_id IN (select job_id from jobs where min_salary>8000);

SELECT first_name, last_name, salary from employees
where salary > ANY (select salary from employees where department_id = 100);

SELECT first_name, last_name, salary from employees
where salary > ALL (select salary from employees where department_id = 100);

SELECT first_name, last_name, salary from employees
where salary > (select avg(salary) from employees);

SELECT e1.first_name, e1.last_name, e1.salary
FROM employees e1
WHERE e1.salary >
(SELECT avg(e2.salary) FROM employees e2
WHERE e2.department_id=e1.department_id);


SELECT first_name, last_name, salary from employees 
where department_id IN
(select department_id from departments where location_id IN
(select location_id from locations where country_id =
(select country_id from countries where country_name='United Kingdom')));

SELECT first_name, last_name, salary, JOB_ID from employees 
where job_id IN (select job_id from jobs where UPPER(job_title) like '%MANAGER%')
AND salary > (select AVG(salary) from employees);

SELECT first_name, last_name, salary from employees
where salary > (select MAX(salary) from employees where first_name = 'David');

