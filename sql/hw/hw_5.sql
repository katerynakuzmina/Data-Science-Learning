select * from employees where INSTR(LOWER(first_name), 'b') != 0;

select * from employees where INSTR(LOWER(first_name), 'a', 1, 2) != 0;

select INSTR(department_name, ' ', 1, 2) from departments;


select department_name, SUBSTR(department_name, 1, INSTR(department_name, ' ')-1) 
from departments 
where INSTR(department_name, ' ') != 0;

select first_name, SUBSTR(first_name, 2, LENGTH(first_name)-2) 
from employees;

select * from employees
where LENGTH(SUBSTR(job_id, INSTR(job_id, '_')+1)) > 3
AND SUBSTR(job_id, INSTR(job_id, '_')+1) != 'CLERK';

select * from employees
WHERE hire_date = TRUNC(hire_date,'MM');

select * from employees
where TO_CHAR(hire_date, 'YYYY') = '2008';

select TO_CHAR(SYSDATE+1, '"Tomorrow is "DdSPTH" day of "Month') info
from dual;

select first_name, hire_date, TO_CHAR(hire_date, 'fmddTH" of " Month ", " YYYY')
from employees;

select first_name, last_name, salary, TO_CHAR(salary+salary*0.2, '$999,999.99')
from employees;

select TO_CHAR(SYSDATE, 'dd/mm/yyyy hh24:MI:SS')now_time, 
TO_CHAR(TO_NUMBER(TO_CHAR(SYSDATE, 'dd'))+1)||'/'||'0'||
TO_CHAR(TO_NUMBER(TO_CHAR(SYSDATE, 'mm'))+1)||'/'||
TO_CHAR(TO_NUMBER(TO_CHAR(SYSDATE, 'YYYY'))+1)||'/'||
TO_CHAR(TO_NUMBER(TO_CHAR(SYSDATE, 'hh24'))+1)||':'||
TO_CHAR(TO_NUMBER(TO_CHAR(SYSDATE, 'MI'))+1)||':'||
TO_CHAR(TO_NUMBER(TO_CHAR(SYSDATE, 'SS'))+1) new_date
from dual;

select first_name, salary, salary + TO_NUMBER('$12,345.55', '$99,999.99')new_salary
from employees;

select first_name, hire_date, ROUND(months_between(
TO_DATE('SEP, 18:45:00 18 2009', 'MON, hh24:MI:SS DD YYYY'), hire_date)) difference
from employees;

select first_name, salary, 
TO_CHAR(salary + salary*NVL(commission_pct, 0), '$999,999.99')full_salary
from employees;


select first_name, last_name, 
NVL2(NULLIF(Length(first_name), Length(last_name)), 
'different  length', 'same length') info
from employees;

SELECT first_name, commission_pct, NVL2(commission_pct, 'Yes', 'No') has_bonus
from employees;

select first_name, 
CASE
WHEN commission_pct is not null THEN commission_pct
WHEN manager_id is not null THEN manager_id
ELSE salary
END info
from employees;

select first_name, salary,
CASE 
WHEN salary <5000 THEN 'Low level'
WHEN salary >=5000 and salary <10000 THEN 'Normal level'
ELSE 'High level'
END "Salary level"
from employees;

select country_name, region_id, 
DECODE(region_id, 1, 'Europe', 2, 'America', 3, 'Asia', 'Africa') region_name
from countries;

select country_name, region_id, 
CASE region_id
WHEN 1 THEN 'Europe'
WHEN 2 THEN 'America'
WHEN 3 THEN 'Asia'
ELSE 'Africa'
END region_name
from countries;

select first_name, salary,
CASE
WHEN salary < 10000 and commission_pct is null THEN 'BAD'
WHEN salary between 10000 and 15000 or commission_pct is not null THEN 'NORMAL'
ELSE 'GOOD'
END conditions
from employees;