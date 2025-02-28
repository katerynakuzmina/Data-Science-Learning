SELECT first_name, last_name, salary, e.department_id, department_name
from employees e, departments d
where e.department_id=d.department_id;


SELECT first_name, last_name, salary, e.department_id, department_name
from employees e, departments d
where e.department_id=d.department_id(+);


SELECT * FROM COUNTRIES, REGIONS;