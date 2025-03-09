CREATE TABLE address (
id integer CONSTRAINT ad_id_un UNIQUE,
country varchar2 (25),
city varchar2 (25)
);

select * from address;

CREATE TABLE friends (
id integer,
name varchar2 (25),
email varchar2 (35),
address_id integer CONSTRAINT f_ad_fr 
REFERENCES address(id) ON DELETE SET NULL,
birthday date,
CONSTRAINT f_n_ch CHECK(LENGTH(name) > 3)
);

CREATE UNIQUE INDEX f_id_in on friends(id);

ALTER TABLE friends ADD CONSTRAINT fr_id_pk PRIMARY KEY (id);

CREATE INDEX fr_email on friends(email);

ALTER TABLE friends MODIFY (email CONSTRAINT fr_email_nn NOT NULL); 

DROP TABLE friends;

DROP TABLE address;