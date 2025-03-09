SELECT 
    p.patient_id, 
    first_name, 
    last_name 
FROM patients p
JOIN admissions a ON (p.patient_id=a.patient_id)
WHERE diagnosis = 'Dementia';


SELECT 
    first_name 
FROM patients 
ORDER BY LENGTH(first_name), first_name;


SELECT 
    COUNT(*), 
    (SELECT COUNT(*) 
        FROM patients 
        WHERE gender = 'F') 
FROM patients
WHERE gender = 'M';


SELECT 
	first_name, 
    last_name, 
    allergies
from patients
where allergies in ('Penicillin', 'Morphine')
order by allergies, first_name, last_name;


SELECT 
	patient_id,
    diagnosis
from admissions
group by patient_id, diagnosis
having count(diagnosis) >1;


SELECT 
	city,
    COUNT(*)
from patients
group by city
ORDER BY COUNT(*) DESC, city;


SELECT 
	first_name, 
    last_name,
    'Patient' AS "role"
FROM patients
UNION ALL
SELECT 
	first_name, 
    last_name,
    'Doctor' AS "role"
FROM doctors;   


SELECT 
	allergies,
    COUNT(*) AS total_diagnosis
from patients
group by allergies
HAVING allergies IS NOT null
order by count(*) DESC;


SELECT 
	first_name,
    last_name,
    birth_date
from patients
where year(birth_date) between 1970 AND 1979
order by birth_date;


SELECT 
	CONCAT(UPPER(last_name), ',', LOWER(first_name))
FROM patients
order by first_name desc;


SELECT 
	province_id,
    SUM(height)
FROM patients
group by province_id
HAVING SUM(height) >= 7000;


SELECT 
	max(weight) - MIN(weight)
FROM patients
WHERE last_name = 'Maroni';


SELECT 
	day(admission_date),
    COUNT(*)
from admissions
group by day(admission_date)
order by COUNT(*) DESC;


SELECT *
from admissions
where 
	patient_id = 542 
    AND admission_date =
		(select MAX(admission_date) 
         from admissions 
         where patient_id = 542);


SELECT 
	patient_id,
    attending_doctor_id,
    diagnosis
from admissions
WHERE patient_id % 2 != 0 AND attending_doctor_id IN (1, 5, 19)
OR attending_doctor_id like '%2%' AND LENGTH(patient_id)=3;



SELECT 
	first_name,
    last_name,
    COUNT(*)
FROM doctors d 
JOIN admissions a 
ON (d.doctor_id=a.attending_doctor_id)
GROUP BY doctor_id;


SELECT 
	doctor_id,
	first_name||' '|| last_name,
    MIN(admission_date),
    MAX(admission_date)
FROM doctors d join admissions a 
ON (a.attending_doctor_id=d.doctor_id)
GROUP BY doctor_id;


SELECT 
	province_name,
    COUNT(*) AS patient_count
FROM patients pat JOIN province_names prov 
ON (pat.province_id=prov.province_id)
GROUP BY province_name
ORDER BY patient_count DESC;


SELECT 
	p.first_name||' '||p.last_name AS patient_name,
    diagnosis,
    d.first_name||' '||d.last_name AS doctor_name
FROM patients p 
	JOIN admissions a ON (p.patient_id=a.patient_id)
    JOIN doctors d ON (d.doctor_id=a.attending_doctor_id);


SELECT 
	first_name,
    last_name,
    COUNT(*)
FROM patients
GROUP BY CONCAT(first_name, ' ', last_name)
HAVING COUNT(*)>1;


SELECT 
	CONCAT(first_name, ' ', last_name) AS patient_name,
    ROUND(height/30.48, 1),
    ROUND(weight*2.205),
    birth_date,
    CASE
    	WHEN gender = 'M' THEN 'MALE'
        ELSE 'FEMALE'
    END AS gender
FROM patients;


SELECT 
	patient_id,
    first_name,
    last_name
FROM patients 
WHERE patient_id NOT IN 
(SELECT patient_id FROM admissions);
    

SELECT 
	MAX(number_of_visits) max_visits,
    MIN(number_of_visits) min_visits,
    ROUND(AVG(number_of_visits), 2) avg_visits
FROM (SELECT COUNT(*) AS number_of_visits 
      FROM admissions
      GROUP BY admission_date);