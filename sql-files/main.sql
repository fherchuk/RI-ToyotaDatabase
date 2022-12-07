USE toyota;

CREATE TABLE ri_toyota(location int, city varchar (45), phone varchar(15), PRIMARY KEY (location));

CREATE TABLE vehicles(VIN char(17), Year int, make varchar (45), model varchar (45), color varchar (45), 
 PRIMARY KEY (VIN));

CREATE TABLE customer(id int NOT NULL, name varchar(45), phone varchar(15), insurance bool,
PRIMARY KEY (id));

CREATE TABLE sales_rep(id varchar(7), name varchar (45), phone varchar(15), location int, sales int,
PRIMARY KEY (id),
foreign key (location) references ri_toyota(location));

CREATE TABLE sales(id int, date varchar(45), agent varchar(7), VIN CHAR(17) NOT NULL, customer int, 
PRIMARY KEY (id), 
foreign key (agent) references sales_rep(id), 
foreign key (VIN) references vehicles(VIN),
foreign	key (customer) references customer(id));

insert into ri_toyota (location, city, phone) values 
('1001', 'Providence', '1234567891'),
('1222', 'Warwick', '1334567891'),
('1103', 'North Kingstown', '1334599991');

insert into vehicles(VIN, year, make, model, color) values 
('1N4AB41D7VC757660', '2022', 'Toyota', 'Camry', 'Red'),
('1JCMR7841JT185472', '2022', 'Toyota', 'Highlander', 'Black'),
('JNKCV51E03M018631', '2022', 'Toyota', 'Camry', 'Silver'),
('4T1SK12E0SU483434', '2022', 'Toyota', 'Tundra', 'Black'),
('5TDZK22C48SA74666', '2022', 'Toyota', 'Corolla', 'White'),
('1N4AB41D7VK331440', '2023', 'Toyota', 'Camry', 'Blue'),
('1THMR7841JT244512', '2021', 'Toyota', 'Highlander', 'Silver'),
('JTEBU5JR0K5678322', '2019', 'Toyota', '4Runner', 'Black'),
('3TMCZ5AN5JM125097', '2018', 'Toyota', 'Tacoma', 'White'),
('JTMC1RFV7ND087252', '2022', 'Toyota', 'Rav4', 'White'),
('1N4AB41D7VY558555', '2023', 'Toyota', 'Camry', 'Cyan'),
('7MUBAAAG2PV037474', '2023', 'Toyota', 'Corlla Cross', 'Black'),
('7MUBAAAG2PV46A141', '2023', 'Toyota', 'Corolla Cross', 'Red'),
('7MUBAAAG2PV45A533', '2023', 'Toyota', 'Corolla Cross', 'Black'),
('7MUBAAAG2PV45C055', '2023', 'Toyota', 'Corolla Cross', 'White'),
('JTMABABA5PA001899', '2023', 'Toyota', 'bZ4X', 'Silver'),
('JTMAAAAA8PA001366', '2023', 'Toyota', 'bZ4X', 'Blue'),
('4T1K31AK1NU581994', '2022', 'Toyota', 'Camry', 'Black'),
('4T1K31AK1NX566223', '2022', 'Toyota', 'Camry', 'Blue'),
('4T1K31AK1TU544816', '2022', 'Toyota', 'Camry', 'White');

insert into customer (id, name, phone, insurance) values
('3285464', 'Joe Shea', '1401555678', 1),
('3371198', 'Mary Smith', '1401578699', 1),
('2370190', 'Greg Andrews', '1401123767', 1),
('3204481', 'Jane Garcia', '14017775577', 0),
('4204544', 'Mary Smith', '14016060066', 1),
('2331988', 'Ashley Young', '14019419941', 0),
('3204112', 'Joe Peters', '14016661337', 0),
('3075155', 'TJ Andersson', '14019898888', 1),
('2322199', 'Greg McKegg', '14010000000', 1),
('3283280', 'Peter Davis', '14011011001', 0),
('3351111', 'Paul David', '14019985589', 1),
('2390420', 'Allison Watson', '14018008135', 1),
('2304878', 'Bethany Dee', '14019914422', 1),
('2304844', 'Marcus Dee', '14019914422', 1);







insert into sales_rep (id, name, phone, location, sales) values 
('S3311PR', 'John Smith', '1401432665', 1001, NULL),
('L0422WA', 'Tyler Ligma', '1401777898', 1222, NULL),
('J1917NK', 'Kevin Jones', '1401156999', 1103, NULL),
('T3100PR', 'Joshua Thomas', '14013456987', 1001, NULL),
('G0420WA', 'John Grossman', '14012202002', 1222, NULL),
('W1402NK', 'Patricia Wallace', '14015551212', 1103, NULL),
('M4899PR', 'Katheryn Mills', '14018844121', 1001, NULL),
('J9955WA', 'Kevin Jones', '14018841888', 1222, NULL),
('T1005NK', 'Tammy Turner', '14019894111', 1103, NULL),
('L2025NK', 'Aiden Lewis', '14015588855', 1103, NULL);

insert into sales (id, date, agent, VIN, customer) values 
('212', '12-01-2022', 'L2025NK', '1N4AB41D7VC757660', '3285464'),
('213', '12-01-2022', 'M4899PR', '1JCMR7841JT185472', '2304878'),
('214', '12-02-2022', 'G0420WA', 'JNKCV51E03M018631', '2322199'),
('215', '12-02-2022', 'T1005NK', '4T1SK12E0SU483434', '2390420'),
('216', '12-02-2022', 'J1917NK', '5TDZK22C48SA74666', '3283280'),
('217', '12-02-2022', 'L2025NK', '1N4AB41D7VK331440', '3283280'),
('218', '12-02-2022', 'T3100PR', '1THMR7841JT244512', '3075155'),
('219', '12-03-2022', 'M4899PR', 'JTEBU5JR0K5678322', '3204112'),
('222', '12-04-2022', 'L2025NK', '3TMCZ5AN5JM125097', '2331988'),
('223', '12-04-2022', 'J9955WA', 'JTMC1RFV7ND087252', '4204544'),
('224', '12-04-2022', 'M4899PR', '1N4AB41D7VY558555', '3204481'),
('226', '12-04-2022', 'L0422WA', '7MUBAAAG2PV037474', '3204481'),
('227', '12-05-2022', 'G0420WA', '7MUBAAAG2PV46A141', '2322199'),
('228', '12-05-2022', 'T3100PR', '7MUBAAAG2PV45A533', '2370190'),
('231', '12-06-2022', 'M4899PR', '7MUBAAAG2PV45C055', '3371198'),	
('232', '12-06-2022', 'L0422WA', 'JTMAAAAA8PA001366', '2304844'),
('233', '12-06-2022', 'L2025NK', 'JTMABABA5PA001899', '3351111'),
('234', '12-06-2022', 'L2025NK', '4T1K31AK1NU581994', '3351111');




DELETE FROM sales WHERE ID = 212 



;

