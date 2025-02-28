SELECT * FROM jobs
WHERE job_id LIKE '%MAN%'
UNION ALL
SELECT * FROM jobs
WHERE job_id LIKE '%MAN%';

SELECT job_id, max_salary FROM jobs
WHERE job_id LIKE '%MAN%'
UNION ALL
SELECT job_title, min_salary FROM jobs
WHERE job_id LIKE '%MAN%';

SELECT job_id, job_title, min_salary FROM jobs
WHERE job_id LIKE '%MAN%'
UNION ALL
SELECT job_id, job_title, min_salary FROM jobs
WHERE job_id LIKE '%MAN%'
ORDER BY min_salary DESC;



SELECT * FROM jobs
WHERE job_id LIKE '%MAN%'
UNION
SELECT * FROM jobs
WHERE job_id LIKE '%MAN%';

SELECT * FROM jobs
WHERE job_id LIKE '%MAN%'
UNION
SELECT * FROM jobs
WHERE job_id LIKE '%MAN%'
ORDER BY 3;

SELECT * FROM jobs 
WHERE min_salary BETWEEN 4500 AND 8000
UNION
SELECT * FROM jobs 
WHERE max_salary BETWEEN 10000 AND 15000;



SELECT * FROM jobs
WHERE job_id LIKE '%MAN%'
INTERSECT
SELECT * FROM jobs
WHERE job_id LIKE '%MAN%';

SELECT * FROM jobs 
WHERE min_salary BETWEEN 4500 AND 8000
INTERSECT
SELECT * FROM jobs 
WHERE max_salary BETWEEN 10000 AND 15000;


SELECT * FROM jobs
WHERE job_id LIKE '%MAN%'
MINUS
SELECT * FROM jobs
WHERE job_id LIKE '%MAN%';


SELECT * FROM jobs 
WHERE min_salary BETWEEN 4500 AND 8000
MINUS
SELECT * FROM jobs 
WHERE max_salary BETWEEN 10000 AND 15000;



SELECT first_name, salary from employees
where first_name like '%a%'
INTERSECT
SELECT first_name, salary from employees
where first_name like '%e%'
MINUS 
SELECT first_name, salary from employees
where first_name like '%l%';

SELECT first_name, salary from employees
where first_name like '%a%'
UNION
(SELECT first_name, salary from employees
where first_name like '%e%'
MINUS 
SELECT first_name, salary from employees
where first_name like '%l%');


select manager_id from employees where department_id = 20
INTERSECT
select manager_id from employees where department_id = 30 
MINUS
select manager_id from employees where department_id = 40;

select department_id dep_id, to_char(null) job_id, sum(salary) from employees
group by department_id
UNION
select to_number(null), job_id, sum(salary) from employees
group by job_id;