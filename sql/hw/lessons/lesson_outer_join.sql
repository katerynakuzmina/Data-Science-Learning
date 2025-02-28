select *  from employees;

SELECT first_name, last_name, salary, department_name
from employees e JOIN departments d ON (e.department_id=d.department_id);


SELECT first_name, last_name, salary, department_name
from employees e LEFT OUTER JOIN departments d ON (e.department_id=d.department_id);


SELECT first_name, last_name, salary, department_name
from departments d LEFT OUTER JOIN employees e ON (e.department_id=d.department_id);


SELECT first_name, last_name, salary, department_name
from employees e RIGHT OUTER JOIN departments d ON (e.department_id=d.department_id);

select country_name, city, street_address
from locations l RIGHT OUTER JOIN countries c ON (l.country_id=c.country_id);


SELECT NVL(first_name, 'no employee'), NVL(last_name,'no employee'), 
NVL(salary, 0), NVL(department_name, 'no department')
from employees e FULL OUTER JOIN departments d ON (e.department_id=d.department_id);
