insert into new_emps
(select employee_id, first_name, hire_date, job_id from employees
where employee_id< 110);

MERGE INTO new_emps ne
USING employees e
ON (ne.emp_id=e.employee_id)
WHEN MATCHED THEN
UPDATE SET ne.start_date = SYSDATE
DELETE where ne.job like '%IT%'
WHEN NOT MATCHED THEN
INSERT (emp_id, name, start_date, job) 
VALUES (employee_id, last_name, hire_date, job_id);

select * from new_emps;
select * from employees;