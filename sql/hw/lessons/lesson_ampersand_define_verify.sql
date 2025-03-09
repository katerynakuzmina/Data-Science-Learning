select first_name, last_name, salary
from employees
where employee_id=&ID;

select first_name, last_name, salary
from employees
where first_name like '%&&letter%'
AND last_name like '%&letter%';
UNDEFINE letter;
DEFINE;
DEFINE letter = a;

