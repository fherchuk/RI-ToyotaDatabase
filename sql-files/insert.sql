insert into ri_toyota
(loc_num, loc_city, loc_phone)
values ('1', 'Providence', '1234567891');

insert into ri_toyota
(loc_num, loc_city, loc_phone)
values ('2', 'Warwick', '1334567891');

insert into ri_toyota
(loc_num, loc_city, loc_phone)
values ('3', 'North Kingstown', '1334599991');

insert into vehicles
(VIN, vehicle_year, make, model, color)
values ('1N4AB41D7VC757660', '2000', 'Toyota', 'Camery', 'Red');

insert into vehicles
(VIN, vehicle_year, make, model, color)
values ('1JCMR7841JT185472', '2010', 'Toyota', 'Highlander', 'Black');

insert into vehicles
(VIN, vehicle_year, make, model, color)
values ('JNKCV51E03M018631', '2009', 'Toyota', 'Camery', 'Silver');

insert into vehicles
(VIN, vehicle_year, make, model, color)
values ('4T1SK12E0SU483434', '2018', 'Toyota', 'Tundra', 'Black');

insert into vehicles
(VIN, vehicle_year, make, model, color)
values ('5TDZK22C48SA74666', '2021', 'Toyota', 'Corolla', 'White');

insert into customer
(customer_id, c_phone, insurance, licence_number)
values ('1', '1401555678', 0, '3285464 ');

insert into customer
(customer_id, c_phone, insurance, licence_number)
values ('2', '1401578699', 1, '3371198');

insert into customer
(customer_id, c_phone, insurance, licence_number)
values ('3', '1401123767', 1, '2370190');

insert into sales_rep
(srep_id, srep_name, srep_number)
values ('1', 'John Smith', '1401432665');

insert into sales_rep
(srep_id, srep_name, srep_number)
values ('2', 'Tyler Ligma', '1401777898');

insert into sales_rep
(srep_id, srep_name, srep_number)
values ('3', 'Kevin Jones', '1401156999');

insert into sales
(sale_id, sale_date)
values ('1', '10-29-2022');

insert into sales
(sale_id, sale_date)
values ('2', '9-10-2022');

insert into sales
(sale_id, sale_date)
values ('3', '9-09-2022');

ALTER TABLE customer
ADD c_name varchar(45);

UPDATE customer
SET c_name = 'John Doe'
WHERE customer_id = '1';

UPDATE customer
SET c_name = 'Dan Johnson'
WHERE customer_id = '2';

UPDATE customer
SET c_name = 'Mike Hawk'
WHERE customer_id = '3';