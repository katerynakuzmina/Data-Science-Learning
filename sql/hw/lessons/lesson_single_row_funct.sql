SELECT * FROM EMPLOYEES 
WHERE LENGTH(FIRST_NAME)>10;

SELECT * FROM EMPLOYEES
WHERE MOD(SALARY, 1000)=0;

SELECT PHONE_NUMBER, SUBSTR(PHONE_NUMBER, 1, 3) "First Number" FROM EMPLOYEES
WHERE PHONE_NUMBER LIKE '___.___.____';

SELECT * FROM EMPLOYEES 
WHERE length(first_name) > 5 and first_name like '%m';

SELECT NEXT_DAY(SYSDATE, 5) FROM DUAL;

SELECT * FROM employees
WHERE MONTHS_BETWEEN(SYSDATE, hire_date) > 150;

select replace(phone_number, '.', '-') from employees;

select upper(first_name), lower(email), initcap(job_id) from employees;

select concat(first_name, salary) from employees;

select hire_date, round(hire_date, 'MM'), round(hire_date, 'YYYY')
from employees;

select RPAD(first_name, 10, '$') as right, LPAD(last_name, 15, '!') as left
from employees;

select first_name, INSTR(first_name, 'a', 1, 2) from employees;

select '!!!HELLO!! MY FRIEND!!!!!!!', TRIM('!' from '!!!HELLO!! MY FRIEND!!!!!!!') from dual;

select salary, salary * 3.1415, ROUND(salary * 3.1415, 0), TRUNC(salary * 3.1415, -3) 
from employees;

select hire_date, ADD_MONTHS(hire_date, 6), LAST_DAY(hire_date) from employees;

select length('21.07.23') from dual;

select trunc(3.1415) from dual;

select ROUND(31465, -2) from dual; 

select MOD(39, 5) from dual; 

select first_name, last_name, salary from employees where MOD(salary, 1000)=0;

select MONTHS_BETWEEN('21.07.23', '21.01.23' ) from dual;

select hire_date, ROUND(hire_date, 'YYYY') from employees;