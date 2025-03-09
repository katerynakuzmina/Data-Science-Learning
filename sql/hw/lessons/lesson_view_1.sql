select * from employees;

create view  emps_with_high_salary3 AS
select first_name, last_name from employees where salary >=12000;

update employees SET salary = 15000 where employee_id = 103;
select * from emp_details_view;
select * from emps_with_high_salary3;

create view fin_emp3 AS
select department_name, SUM(salary) sum_salary from employees e
JOIN departments d ON (d.department_id=e.department_id)
GROUP BY department_name;

select * from fin_emp3;

insert into fin_emp3 values('abra-kadabra', 100000);
update fin_emp3 set department_name = 'abra-kadabra' where sum(salary) > 5000;

create view v105 AS
select SUBSTR(name, 2) name, course from students;
select * from v105;
insert into v105 values ('Kolya', 3);
delete from v105 where name = 'aur';

select * from students;
drop view v105;
create view v106 as select distinct name, course from students;
