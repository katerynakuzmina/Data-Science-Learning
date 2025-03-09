select * from employees;

CREATE TABLE students (
student_id integer,
name varchar2 (15),
start_date date DEFAULT ROUND(SYSDATE),
scholarship number (6, 2),
avg_score number (4, 2) default 5
);

INSERT INTO students (student_id, name, start_date, scholarship, avg_score)
VALUES (1, 'Zaur', TO_DATE('18-SEP-19'), 1500.3, 7.8);
INSERT INTO students (student_id, name, start_date, scholarship, avg_score)
VALUES (2, 'Ivan', TO_DATE('19-SEP-19'), 800.356, 8);
INSERT INTO students (student_id, name, scholarship)
VALUES (3, 'Nina', 555);

select * from students;


select * from new_emps2;
CREATE TABLE new_emps2 AS (SELECT employee_id, first_name, last_name,
salary, department_id FROM employees);

CREATE TABLE new_dep AS (SELECT department_name, MAX(salary) max_salary,
MIN(salary) min_salary from employees e JOIN departments d
ON (e.department_id=d.department_id) group by department_name);

select * from new_dep;

CREATE TABLE regions2 AS (SELECT * FROM regions WHERE 1=2);




SELECT * from students;

ALTER TABLE students ADD (course number DEFAULT 3);

ALTER TABLE students MODIFY (avg_score number(5, 3));

ALTER TABLE students MODIFY (start_date date DEFAULT null);

INSERT INTO students (student_id, name)
VALUES (4, 'Vova');

ALTER TABLE students DROP COLUMN scholarship;

ALTER TABLE students SET UNUSED COLUMN start_date;
ALTER TABLE students DROP UNUSED COLUMNS;

ALTER TABLE students RENAME COLUMN student_id TO id;

ALTER TABLE students READ ONLY;

DROP TABLE students;

TRUNCATE TABLE students;