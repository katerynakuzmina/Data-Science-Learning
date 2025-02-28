select emp1.employee_id, emp1.first_name, emp1.manager_id,
emp2.employee_id, emp2.first_name
from employees emp1 JOIN employees emp2 
ON (emp1.manager_id = emp2.employee_id)
group by emp2.first_name;

select emp2.first_name manager_name, count(*)
from employees emp1 JOIN employees emp2 
ON (emp1.manager_id = emp2.employee_id)
group by emp2.first_name
order by count(*);