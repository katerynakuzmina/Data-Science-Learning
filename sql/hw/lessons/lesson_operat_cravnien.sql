SELECT first_name, last_name, salary from employees where salary = 17000;

SELECT first_name, salary from employees where last_name = 'King';

select * from employees where hire_date = '21.09.05';

select * from employees 
where 'Dr David Austin' = 'Dr '||first_name||' '||last_name;

select * from job_history 
where start_date + 364 = end_date;

select * from employees;

select first_name, last_name, salary from employees where salary > 10000;

select first_name, last_name from employees
where salary between 4000 and 17000;

select * from employees where first_name between 'A' and 'E';

select first_name, last_name from employees 
where salary >=4000 and salary <=17000;

select * from departments where location_id in (1700, 2400, 1500);

select * from employees where commission_pct is null;
