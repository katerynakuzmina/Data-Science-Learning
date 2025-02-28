select * from regions;

select * from countries;


select c.country_name, c.country_id, r.region_name, region_id 
from regions r NATURAL JOIN countries c;

select * from employees where department_id = 90 AND manager_id = 100;
select * from departments where department_id = 90 AND manager_id = 100;

select first_name, last_name, salary, department_name, department_id, manager_id
from employees NATURAL JOIN departments;

select * from employees;
select * from job_history;

select * from employees NATURAL JOIN job_history;