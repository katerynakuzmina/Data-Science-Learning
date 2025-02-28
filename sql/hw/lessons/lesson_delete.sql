select * from employees;

delete from new_emps;

insert into new_emps (select employee_id, first_name, hire_date, job_id
from employees);

select * from new_emps;

delete from new_emps;

delete from new_emps where emp_id = 210;

delete from new_emps where job like '%CLERK%' OR name is null;

select * from departments;

delete from new_emps where job IN 
(select distinct job_id from employees where department_id IN
(select department_id from departments where manager_id = 100));