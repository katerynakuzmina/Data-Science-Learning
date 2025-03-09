select * from employees;
drop table students;
CREATE TABLE students (
id number,
name varchar (15),
course number,
faculty_id number
);

CREATE INDEX in1 ON students(id);

select * from students;
insert into students values(1, 'Zaur', 3);
insert into students values(2, 'Misha', 2);
insert into students values(2, 'Lesha', 5);
insert into students values(3, 'Lesha', 3);

CREATE UNIQUE INDEX in2 ON students(name);
CREATE INDEX in3 ON students(name, id);

CREATE TABLE faculties (
id number,
name varchar (15)
);

CREATE UNIQUE INDEX st_in1 ON students(id);
CREATE UNIQUE INDEX f_in1 ON faculties(id);
CREATE UNIQUE INDEX st_in2 ON students(course);
CREATE INDEX st_in3 ON students(name);

ALTER TABLE students ADD CONSTRAINT st_pk PRIMARY KEY (id);
ALTER TABLE faculties ADD CONSTRAINT f_pk PRIMARY KEY (id);
ALTER TABLE students ADD CONSTRAINT st_un UNIQUE (course);
ALTER TABLE students ADD CONSTRAINT st_fk FOREIGN KEY (faculty_id)
REFERENCES faculties(id);