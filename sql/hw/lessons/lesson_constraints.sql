CREATE TABLE students (
id number,
name varchar (15),
course number CONSTRAINT ch CHECK (course>0 AND course<6),
faculty_id integer REFERENCES faculties ON DELETE SET NULL
);

DROP TABLE students;

CREATE TABLE faculties (
id number PRIMARY KEY,
name varchar (15)
);

ALTER TABLE students MODIFY (id CONSTRAINT at_id_unique UNIQUE);
ALTER TABLE students MODIFY (id UNIQUE);

INSERT INTO faculties VALUES (1, 'CS');

INSERT INTO faculties VALUES (2, 'Marketing');
commit;
INSERT INTO faculties VALUES (3, 'Phihology');
DROP TABLE faculties;

select * from faculties;

ALTER TABLE faculties ADD UNIQUE(id);

select * from students;

INSERT INTO students VALUES
(1, 'Zaur', 3, 1);

INSERT INTO students VALUES
(2, 'Ivan', 2, 2);

INSERT INTO students VALUES
(3, 'Misha', 1, 1);

DELETE FROM faculties where id=3;

DELETE FROM faculties where id=1;