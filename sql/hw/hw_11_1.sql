CREATE TABLE friends AS 
(SELECT employee_id id, first_name name, last_name surname
FROM employees WHERE commission_pct IS NOT NULL);

select * from friends;

ALTER TABLE friends ADD (email varchar2(18));

ALTER TABLE friends MODIFY (email varchar2(18) DEFAULT 'no email');

INSERT INTO friends (id, name, surname) VALUES (302, 'Vika', 'Loboda');

ALTER TABLE friends RENAME COLUMN id TO friends_id;

DROP tABLE friends;

CREATE TABLE friends (
id integer,
name varchar2(30),
surname varchar2(40),
email varchar2(30),
salary number (8, 2) DEFAULT 0,
birthday date DEFAULT ROUND(SYSDATE)
);

select * from friends;

INSERT INTO friends VALUES (1, 'Kate', 'Nos', 'katenos@com.pl', 20000.00, 
TO_DATE('01-JAN-89', 'DD-MON-RR'));

INSERT INTO friends (id, name, surname, email) VALUES (2, 'Jack', 'Hure', 
'jackhek@com.pl');
COMMIT;

ALTER TABLE friends DROP COLUMN salary;

ALTER TABLE friends SET UNUSED COLUMN email;

ALTER TABLE friends SET UNUSED COLUMN birthday;

ALTER TABLE friends DROP UNUSED COLUMNS;

ALTER TABLE friends READ ONLY;

select * from friends;

INSERT INTO friends VALUES (3, 'Jay', 'Miki');

TRUNCATE TABLE friends;

DROP TABLE friends;