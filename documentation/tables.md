# Tietokantataulujen CREATE TABLE -lauseet

CREATE TABLE account ( 
	id INTEGER NOT NULL,   
	date_created DATETIME,   
	date_modified DATETIME,   
	name VARCHAR(144) NOT NULL,   
	username VARCHAR(144) NOT NULL,   
	password VARCHAR(144) NOT NULL,   
	PRIMARY KEY (id)  
)

CREATE TABLE employee (
	id INTEGER NOT NULL, 
	name VARCHAR(144), 
	role VARCHAR(144), 
	"hoursPerDay" INTEGER, 
	"hoursPerWeek" INTEGER, 
	PRIMARY KEY (id)
)

CREATE TABLE busyness (
	id INTEGER NOT NULL, 
	name VARCHAR(144), 
	laakareita INTEGER, 
	sairaanhoitajia INTEGER, 
	perushoitajia INTEGER, 
	PRIMARY KEY (id)
)

CREATE TABLE hour (
	id INTEGER NOT NULL, 
	date DATE, 
	start INTEGER, 
	busyness_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(busyness_id) REFERENCES busyness (id)
)

CREATE TABLE employee_hours (
	employee_id INTEGER, 
	hour_id INTEGER, 
	FOREIGN KEY(employee_id) REFERENCES employee (id), 
	FOREIGN KEY(hour_id) REFERENCES hour (id)
)

