ALTER TABLE sales ADD srep_id INT NOT NULL;
ALTER TABLE sales ADD CONSTRAINT fk_srep FOREIGN KEY (srep_id) REFERENCES sales_rep(srep_id);

UPDATE sales
SET srep_id = '1'
WHERE sale_id = '1';

UPDATE sales
SET srep_id = '1'
WHERE sale_id = '2';

UPDATE sales
SET srep_id = '2'
WHERE sale_id = '3';

ALTER TABLE sales ADD VIN CHAR(17) NOT NULL;
ALTER TABLE sales ADD CONSTRAINT fk_vin FOREIGN KEY (VIN) REFERENCES vehicles(VIN);

SELECT * from sales;

UPDATE sales
SET VIN = '5TEPM62N53Z204215'
WHERE sale_id = '1';

UPDATE sales
SET VIN = 'JT4RN55D0H7025002'
WHERE sale_id = '2';

UPDATE sales
SET VIN = '4T3ZA3BB7DUO63957'
WHERE sale_id = '3';

SELECT * from ri_toyota;

ALTER TABLE vehicles ADD loc_num INT NOT NULL;
ALTER TABLE vehicles ADD CONSTRAINT fk_vehicles FOREIGN KEY (loc_num) REFERENCES ri_toyota(loc_num);

SELECT * from vehicles;

UPDATE vehicles
SET loc_num = '1'
WHERE VIN = '1JCMR7841JT185472';

UPDATE vehicles
SET loc_num = '1'
WHERE VIN = '1N4AB41D7VC757660';

UPDATE vehicles
SET loc_num = '3'
WHERE VIN = '4T1SK12E0SU483434';

UPDATE vehicles
SET loc_num = '2'
WHERE VIN = '5TDZK22C48SA74666';

UPDATE vehicles
SET loc_num = '3'
WHERE VIN = 'JNKCV51E03M018631';

ALTER TABLE sales ADD customer_id INT NOT NULL;
ALTER TABLE sales ADD CONSTRAINT fk_customerid FOREIGN KEY (customer_id) REFERENCES customer(customer_id);

UPDATE sales
SET customer_id = '2'
WHERE sale_id = '1';

UPDATE sales
SET customer_id = '1'
WHERE sale_id = '2';

UPDATE sales
SET customer_id = '3'
WHERE sale_id = '3';

ALTER TABLE sales ADD loc_num INT NOT NULL;
ALTER TABLE sales ADD CONSTRAINT fk_locnum FOREIGN KEY (loc_num) REFERENCES ri_toyota(loc_num);

ALTER TABLE sales_rep ADD loc_num INT NOT NULL;
ALTER TABLE sales_rep ADD CONSTRAINT fk_locnumb FOREIGN KEY (loc_num) REFERENCES ri_toyota(loc_num);

UPDATE sales_rep
SET loc_num = '1'
WHERE srep_id = '1';

UPDATE sales_rep
SET loc_num = '2'
WHERE srep_id = '2';

UPDATE sales_rep
SET loc_num = '3'
WHERE srep_id = '3';

UPDATE sales
SET loc_num = '1'
WHERE sale_id = '1';

UPDATE sales
SET loc_num = '1'
WHERE sale_id = '2';

UPDATE sales
SET loc_num = '2'
WHERE sale_id = '3';

