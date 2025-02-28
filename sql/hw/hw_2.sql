select * from regions;

select employee_id, first_name, last_name, salary, department_id
from employees;

select employee_id, email, (hire_date - 7)+1 "One week before hire date" 
from employees;

select first_name||'('||job_id||')' "our_employees" from employees;

select DISTINCT first_name from employees;

select job_id, 'min='||min_salary||', max='||max_salary as info, 
max_salary as max, max_salary*2-000 as new_salary from jobs;

select 'Peter''s dog is very clever' from dual;

select q'<Peter's dog is very clever>' from dual;

select 100*365.25*24*60*60 from dual;