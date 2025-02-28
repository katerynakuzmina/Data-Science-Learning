select first_name, last_name, salary, department_name, 
e.manager_id emp_manager, d.manager_id dep_manager, 
department_id
from employees e JOIN departments d USING(department_id);


select first_name, last_name, jh.job_id, start_date, end_date
from employees JOIN job_history jh USING(employee_id);