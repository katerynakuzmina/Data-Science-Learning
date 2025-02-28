select TO_CHAR(18, '99999') from dual;
select TO_CHAR(18, '099999') from dual;
select TO_CHAR(18.35, '099999.999') from dual;
select TO_CHAR(1234567, '099,999,999') from dual;
select TO_CHAR(12345, '99,999,999') from dual;
select TO_CHAR(18,'$999') from dual;


select first_name, salary*1.1111111, TO_CHAR(salary*1.1111111, '$999,999.99'),
TO_CHAR(salary*1.1111111, '$9,999.99') 
from employees;


select TO_CHAR(SYSDATE, 'Y') from dual;

select TO_CHAR(SYSDATE, 'MON') from dual;

select TO_CHAR(SYSDATE, 'YEAR') from dual;

SELECT 'my colleague with ID = '||employee_id||' and job_id '||job_id||
' joined us on ' || TO_CHAR(hire_date, 'Day "the "ddTH "of " fmMonth YYYY')
from employees;

select TO_DATE('08-MAR-2025') from dual;

select TO_CHAR(TO_DATE('28-Sep-19 15:16:17', 'dd-Mon-RR HH24:MI:SS'),
'dd-Mon-RR HH24:MI:SS') from dual;

select * from employees where hire_date > TO_DATE('01-JAN-05', 'dd-MON-RR');

select TO_CHAR(TO_DATE('08-MAR-2025', 'dd-MON-YYYY'), 'Month') from dual;

select TO_CHAR(TO_DATE('15?1987$17$18$19/09', 'hh24?YYYY$MI$ss$DD/mm'),
'dd-MON-yyyy hh24:mi:ss') alias from dual;

select TO_NUMBER('4,555.77', '999,999.999') from dual;

select TO_NUMBER('<4555.77>', '99999.999PR') from dual;

select first_name, LENGTH(first_name), ROUND(123.56438466593, LENGTH(first_name))
from employees;

select first_name, last_name, phone_number,
TO_NUMBER(SUBSTR(phone_number, INSTR(phone_number, '.') + 1), '999.9999') *
10000 form_numb
from employees where employee_id < 130;

select NVL(18, 19) from dual;

select NVL(0, 19) from dual;

select first_name, NVL(commission_pct, 0) from employees;

select first_name, NVL(SUBSTR(first_name, 6), 'name is too short') from employees;

select first_name, SUBSTR(first_name, 6) from employees;

select first_name, NVL2(commission_pct, commission_pct, 0) from employees;

select first_name, commission_pct, NVL(salary*commission_pct, 500) from employees;

select NVL2(null, 18, 19) from dual;

select nullif(18, 18) from dual;

select nullif(17, 18) from dual;

select nullif(18, 18) from dual;

select nullif(TO_DATE('18-SEP-87'), TO_DATE('18/SEP/87')) from dual;

select country_id, country_name,
NVL2(NULLIF(country_id, UPPER(SUBSTR(country_name, 1,2))), 'not the same', 'the same')
from countries;

select COALESCE(1, null, 2) from dual;

select first_name, commission_pct, manager_id, salary,
COALESCE(comission_pct, manager_id, salary) info 
from employees;

select DECODE(3*4, 13, 'trynadcat', 14, 'cetyrnacat', 12, 'dvenadcat') from dual;

select DECODE(3*4, 13, 'trynadcat', 14, 'cetyrnacat', 18, 'vosemnacat', 'net sovppadenij') from dual; OUTPUT:net sovppadenij

select DECODE(2+2*2, 5, 'five', 12/2, 'six1', 6, 'six2') from dual; 

select 
CASE 3*4
WHEN 12 THEN 100
END
from dual;


select 
CASE 3*4
WHEN 11 THEN 'eleven'
WHEN 12 THEN 'twelve1'
WHEN 24/2 THEN 'twelve2'
END
from dual;

select first_name,
CASE LENGTH(first_name)
WHEN 4 THEN 'Very short name'
WHEN 5 THEN 'short name'
WHEN 6 THEN 'middle length name'
WHEN 7 THEN 'long name'
WHEN 8 THEN 'Very long name'
ELSE 'Ups, the legth is not known'
END
from employees;

select first_name, commission_pct,salary*10,
CASE
WHEN LENGTH(first_name)<= 5 THEN 'The 1 condition matches'
WHEN salary*10 >100000 THEN 'The 2 condition matches'
WHEN commission_pct is not null THEN 'The 3 condition matches'
ELSE 'No condition match'
END case_statement
from employees;