select * from employees;

UPDATE employees SET salary=10000 where employee_id=100;

UPDATE employees SET salary=salary*2 where employee_id=100;

UPDATE employees SET salary=27000, job_id='IT_PROG' where employee_id=100;

UPDATE employees SET salary=8000 where employee_id<105;

UPDATE employees SET salary=8000;

select * from employees;

UPDATE employees SET salary=5000 where department_id=
(select department_id from departments where department_name='Marketing');

UPDATE employees SET salary= (select MAX(salary) from employees),
hire_date = (select MIN(start_date) from job_history) 
where employee_id=180;