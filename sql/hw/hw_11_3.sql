CREATE TABLE emp1000 AS
(SELECT first_name, last_name, salary, department_id FROM employees);

CREATE FORCE VIEW v1000 AS
(SELECT first_name, last_name, salary, department_name, city 
FROM emp1000 e JOIN departments d ON (e.department_id=d.department_id));

ALTER TABLE emp1000 ADD (city varchar2(30));
ALTER VIEW v1000 compile;

select * from v1000;

CREATE SYNONYM syn1000 for v1000;
DROP SYNONYM syn1000;

DROP TABLE emp1000;

CREATE SEQUENCE seq1000 start with 12 increment by 4 maxvalue 200 cycle;
ALTER SEQUENCE seq1000 nomaxvalue nocycle;

select * from employees;
select seq1000.nextval from dual;

INSERT INTO employees (employee_id, last_name, email, hire_date, job_id)
VALUES (seq1000.nextval, 'Rogozov', UPPER('rogozov'), TO_DATE('12-JAN-2019',
'DD-MON-YYYY'), UPPER('it_prog'));

INSERT INTO employees (employee_id, last_name, email, hire_date, job_id)
VALUES (seq1000.nextval, 'Morozov', UPPER('morozov'), TO_DATE('12-JAN-2017',
'DD-MON-YYYY'), UPPER('st_clerk'));
COMMIT;