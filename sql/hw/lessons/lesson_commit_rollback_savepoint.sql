DELETE FROM new_emps where name = 'Kuzmina';
COMMIT;


DELETE FROM new_emps;

select * FROM new_emps;

INSERT INTO new_emps
(SELECT employee_id, last_name, hire_date, job_id FROM employees);
COMMIT;

DELETE FROM new_emps where name= 'Kuzmina';
ROLLBACK;
INSERT INTO new_emps VALUES(1000, 'Igor', sysdate, 'IT_PROG');
SAVEPOINT s1;
UPDATE new_emps SET emp_id = 3000 where emp_id=100;
SAVEPOINT s2;
DELETE FROM new_emps where emp_id=101;
ROLLBACK TO SAVEPOINT s2;
ROLLBACK TO SAVEPOINT s1;
commit;

INSERT INTO new_emps
(SELECT employee_id, last_name, hire_date, job_id FROM employees
where employee_id < 110);

select * FROM new_emps FOR UPDATE;
COMMIT;