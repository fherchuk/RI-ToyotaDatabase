/* Get number of sales made by
sales representative with srep_id = '1'
*/
SELECT srep_id, COUNT(srep_id) AS Num_Sales
FROM sales
WHERE srep_id = '1';

/* Show all selected attributes of vehicle(s)
from all vehicles from the Providence location
(loc_num = '1')
*/
SELECT vehicle_year, make, model, color
FROM vehicles
WHERE loc_num = '1';

/* Left join from customer table -> sales
table on customer id showing customer name, customer id,
VIN of vehicle purchased, date purchased
*/
SELECT customer.c_name, customer.c_phone, customer.licence_number, sales.VIN, sales.sale_date
FROM customer
LEFT JOIN sales ON customer.customer_id=sales.customer_id
ORDER BY customer.c_name;

/* Create view 'Black_Vehicles' to show
year, make, model, location number of
all black vehicles in inventory
*/
CREATE VIEW Black_Vehicles AS
SELECT vehicle_year, make, model, loc_num
FROM vehicles
WHERE color = 'Black';

SELECT * FROM Black_Vehicles;

/* Right join from ri_toyota table -> vehicles
table on location number showing city, location phone,
vehicle year, make, model, and color. Order results by
city, year.
*/
SELECT ri_toyota.loc_city, ri_toyota.loc_phone, vehicles.vehicle_year, vehicles.make, vehicles.model, vehicles.color
FROM ri_toyota
RIGHT JOIN vehicles ON ri_toyota.loc_num = vehicles.loc_num
ORDER BY ri_toyota.loc_city, vehicles.vehicle_year;

