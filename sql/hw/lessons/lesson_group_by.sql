select count(*) from employees where salary > 5000;

select count(commission_pct) from employees;

select count(NVL(commission_pct, 0)) from employees;

select count(distinct first_name) from employees;

SELECT sum(salary) from employees;

select sum('7') from employees;

SELECT sum(sysdate- hire_date) from employees;
SELECT AVG(salary) from employees;
select AVG(7) from employees;

select AVG(NVL(commission_pct, 0)) from employees;

select MIN(salary), MAX(salary) from employees where department_id = 50;

select department_id, COUNT(*) from employees group by department_id order by 1, 2;

select job_id, COUNT(*), ROUND(AVG(salary)), MIN(salary), MAX(salary)
from employees
where LENGTH(first_name) > 4 and salary > 5000
group by job_id
ORDER BY job_id, AVG(salary);

select TO_CHAR(hire_date, 'Month'), count(*) from employees
group by TO_CHAR(hire_date, 'Month');

select department_id, count(*) from employees
group by department_id order by department_id;

select job_id, count(*) from employees
group by job_id order by job_id;

select department_id, job_id, count(*) from employees
group by department_id , job_id
order by department_id;

select department_id, manager_id, count(*) from employees
group by department_id , manager_id
order by department_id , manager_id;

select job_id, TO_CHAR(hire_date, 'yyyy') year, sum(salary)
from employees
where job_id IN('ST_CLERK', 'SA_REP', 'SH_CLERK') and employee_id > 115
group by job_id, TO_CHAR(hire_date, 'yyyy')
order by job_id, year;

select department_id, count(*) from employees
group by department_id
HAVING count(*) > 3
order by department_id;


select department_id, count(*), ROUND(AVG(salary)) from employees
where LENGTH(first_name)>4
group by department_id
HAVING count(*) > 3 OR ROUND(AVG(salary)) > 5000
order by department_id;

select department_id, AVG(salary)
from employees
group by department_id;

select SUM(AVG(salary))
from employees
group by department_id;
