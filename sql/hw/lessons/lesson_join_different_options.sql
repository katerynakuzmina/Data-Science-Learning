select * from regions;
select * from employees;
select * from countries;
select * from locations;
select * from job_history;
select * from departments;
select * from jobs;

select first_name, jh.job_id, start_date, end_date, department_name
from employees e
JOIN job_history jh ON (e.employee_id=jh.employee_id)
JOIN departments d ON (jh.department_id=d.department_id);

select * from locations NATURAL JOIN countries NATURAL JOIN regions;

select * from locations JOIN countries USING
(country_id) JOIN regions USING (region_id);

select department_name, min(salary), max(salary)
from employees e JOIN departments d ON (e.department_id=d.department_id)
group by department_name order by department_name DESC;

select first_name, salary, min_salary, max_salary
from employees e JOIN jobs j ON (e.job_id=j.job_id AND salary*2 < max_salary);

select first_name, salary, min_salary, max_salary
from employees e JOIN jobs j ON (e.job_id=j.job_id AND salary = min_salary);

select first_name, salary, min_salary, max_salary
from employees e JOIN jobs j ON (e.job_id=j.job_id AND salary between min_salary+2000 AND max_salary-3000);