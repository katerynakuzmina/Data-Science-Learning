CREATE SEQUENCE s1;
select s1.nextval from dual;
select s1.currval from dual;

DROP TABLE STUDENTS;

CREATE TABLE students (
id number,
name varchar (25),
course number,
faculty_id integer
);

drop table faculties;

create table faculties (
id number,
name varchar2 (15)
);

CREATE SEQUENCE seq_st;
CREATE SEQUENCE seq_faculty start with 20 increment by 5;

insert into faculties values (seq_faculty.nextval, 'IT');
insert into faculties values (seq_faculty.nextval, 'Marketing');
insert into faculties values (seq_faculty.nextval, 'Philologi');
select * from faculties;

insert into students values (seq_st.nextval, 'Zaur', 3, 20);
insert into students values (seq_st.nextval, 'Masha', 2, seq_faculty.currval);
alter sequence seq_st increment by 5;
insert into students values (seq_st.nextval, 'Kolia', 3, 20);
insert into students values (seq_st.nextval, 'Vasya', 1, 25);

select * from students;

create sequence s4 increment by 2 maxvalue 17 cycle cache 3;
select s4.nextval from dual;

create sequence s5 start with 5 increment by 4 maxvalue 17 cycle cache 2;

select s5.nextval from dual;

create sequence s6 start with 7 increment by 4 maxvalue 17 cycle cache 2;

select s6.nextval from dual;