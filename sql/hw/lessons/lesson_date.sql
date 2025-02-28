select * from employees;

select * from sys.nls_session_parameters;

select last_day(sysdate) from dual;

select hire_date, last_day(hire_date)-hire_date prorabotal from employees;

SELECT hire_date, TRUNC(hire_date, 'YYYY') from employees
where employee_id in (120, 121);
