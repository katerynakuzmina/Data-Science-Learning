select first_name, last_name, jh.job_id, start_date, end_date, 
employees.employee_id, jh.employee_id
from employees JOIN job_history jh ON(employees.employee_id=jh.employee_id);

select * from departments JOIN regions ON
(region_id*10 = department_id);

select first_name, last_name, jh.job_id, start_date, end_date
from employees e JOIN job_history jh ON
(e.employee_id=jh.employee_id AND e.department_id = jh.department_id);

select first_name, last_name, department_name
from employees join departments ON 
(employee_id = departments.manager_id);