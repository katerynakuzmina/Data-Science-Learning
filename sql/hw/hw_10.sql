CREATE TABLE locations2 AS (SELECT * FROM locations WHERE 1=2);

select * from locations2;
select * from locations;

INSERT INTO locations2 
(SELECT * FROM locations where location_id IN (1000, 1100));
COMMIT;

DELETE FROM locations2 WHERE location_id IN (1000, 1100);
COMMIT;

INSERT INTO locations2 VALUES
(2000, INITCAP('125 lavita resjera'), 
TO_CHAR(67599), INITCAP('paris'), null, UPPER('fr'));
INSERT INTO locations2 VALUES
(2100, INITCAP('1200 bonita le manta'), 
TO_CHAR(76554), INITCAP('monreal'), null, UPPER('fr'));
COMMIT;

INSERT INTO locations2 VALUES
(3000, INITCAP('00234 Revea'), 
TO_CHAR(67576), INITCAP('roma'), null, UPPER('it'));
INSERT INTO locations2 VALUES
(3100, INITCAP('88776 Levale'), 
TO_CHAR(76768), INITCAP('ROMA'), null, UPPER('IT'));
COMMIT;

INSERT INTO locations2
(SELECT * FROM locations 
WHERE LENGTH(state_province)>9 AND state_province IS NOT NULL);
COMMIT;

CREATE TABLE locations4europe AS (SELECT * FROM locations WHERE 1=2);
select * from countries;
select * from locations4europe;

SELECT country_id, region_id FROM countries where region_id = 1;

INSERT ALL
WHEN 1=1 THEN 
INTO locations2 VALUES (location_id, street_address, postal_code,
city, state_province, country_id)
WHEN country_id IN 
(SELECT country_id FROM countries where region_id = 1) THEN
INTO locations4europe (location_id, street_address, city, country_id) 
VALUES (location_id, street_address, city, country_id)
SELECT * FROM locations;
COMMIT;

UPDATE locations2 
SET postal_code = 100001 
WHERE postal_code IS NULL;
ROLLBACK;

UPDATE locations2
SET postal_code = 
(SELECT postal_code FROM locations where location_id = 2600)
WHERE postal_code IS null;
COMMIT;

DELETE FROM locations2 
WHERE country_id = 'IT';

select * from locations2;
SAVEPOINT s1;

UPDATE locations2 
SET street_address = 'Sezam st. 18'
WHERE location_id > 2500;
SAVEPOINT s2;

DELETE FROM locations2
WHERE street_address = 'Sezam st. 18';
ROLLBACK TO s1;
COMMIT;