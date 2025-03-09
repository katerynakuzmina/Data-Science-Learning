CREATE TABLE students (
id number,
name varchar (15),
course number
);

INSERT INTO students VALUES (1, 'Zaur', 3);
INSERT INTO students VALUES (2, 'Misha', 2);
INSERT INTO students VALUES (3, 'Kolya', 4);
INSERT INTO students VALUES (4, 'Vasya', 5);
INSERT INTO students VALUES (5, 'Petya', 1);

create or replace VIEW fin_emp3 AS select * from students;

select * from fin_emp3;

