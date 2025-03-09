select * from employees;
select * from hr.employees;
select * from hr.employees@orclpdb2;

select * from students;
create SYNONYM syn1 for students;

select * from syn1;

delete from syn1 where id=5;

create PUBLIC SYNONYM syn1 for employees;

drop PUBLIC synonym syn1;


