CREATE DATABASE proj;
USE proj;

CREATE TABLE ri_toyota(loc_num int, loc_city varchar (45), loc_phone int, PRIMARY KEY (loc_num));

CREATE TABLE vehicles(VIN char(17), vehicle_year int, make varchar (45), model varchar (45), color varchar (45), PRIMARY KEY (VIN));

CREATE TABLE customer(customer_id int NOT NULL, c_phone int, insurance bool, licence_number int, PRIMARY KEY (customer_id));

CREATE TABLE sales_rep(srep_id int, srep_name varchar (45), srep_number int, PRIMARY KEY (srep_id));

CREATE TABLE sales(sale_id int, sale_date varchar(45), PRIMARY KEY (sale_id));

SELECT * from ri_toyota;

SELECT * from vehicles;

SELECT * from customer;

SELECT * from sales_rep;

SELECT * from sales;