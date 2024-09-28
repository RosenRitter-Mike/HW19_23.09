'''

1.
הסבר מה עושה CASCADE DELETE ON
במה זה שונה מ- FK רגיל?
האם הפיצ'ר מגדיל /מקטין בטיחות?
_________________________________________________________________________________
Use CASCADE DELETE ON if you want rows deleted in a child table when corresponding rows are deleted in the parent table.
Thus it allows you to reduce the quantity of SQL statements you need to perform delete actions.
If you do not specify cascading deletes, the default behavior of the database Foreign Key prevents you from deleting
data in a table if other tables reference it. This feature lowers security as it enables deletion when it is by default
disabled.

'''

'''

2.
הסבר מה עושה הקוד?
מה עושה::numeric?
מה עושהRANDOM?ROUND?
מה עושהGENERATE_SERIES?
________________________________________________________________________________
What the code does:
- A table called random_numbers is created.
- 10 random decimal numbers between 0 and 100 are inserted into the random_value column.
- All rows in the table are retrieved.
- 3 random rows from the table are selected.
- The random_value of the row with id = 1 is updated to a new random value.
- All rows are retrieved again, showing the update.

What numeric:: does:
It casts the number as numeric data type ((RANDOM() * 100)::numeric).
 
What ROUND(RANDOM does:
It ROUNDS to the nearest number the random number returned by RANDOM() function.

What generate_series does:
allows you to generate a set of data starting at some point, ending at another point, and optionally set the 
incrementing value. 
From https://www.postgresql.org/docs/current/functions-srf.html (PostgresSQL documentation)
generate_series ( start numeric, stop numeric [, step numeric ] ) → setof numeric
Generates a series of values from start to stop, with a step size of step. step defaults to 1.

'''
'''
3.
הסבר מה כל שאילתא עושה?
______________________________________________________________________________
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    sale_amount DECIMAL(10, 2),
    sale_timestamp TIMESTAMP
);

-- Insert sample data with timestamps
INSERT INTO sales (product_name, sale_amount, sale_timestamp) VALUES
('Laptop', 1200.50, '2024-01-10 10:30:00'),
('Smartphone', 800.00, '2024-01-15 14:45:00'),
('Tablet', 450.75, '2024-02-05 09:00:00'),
('Monitor', 250.00, '2024-03-10 11:15:00'),
('Keyboard', 50.00, '2024-03-12 16:30:00');
______________________________________________________________________________
SELECT * FROM sales
WHERE sale_timestamp >= '2024-03-01 00:00:00'
AND sale_timestamp < '2024-04-01 00:00:00';

- Returns the sales/purchases made in March

SELECT * FROM sales
WHERE EXTRACT(DOW FROM sale_timestamp) IN (0, 6);

- Returns sales made on Sunday(0) or Saturday(6)

SELECT * FROM sales
WHERE sale_timestamp >= NOW() - INTERVAL '7 days';

- Returns the sales made in the last week

SELECT * FROM sales
WHERE EXTRACT(HOUR FROM sale_timestamp) BETWEEN 9 AND 17;

- Returns sales made between 9 AM and 5 PM 

SELECT DATE(sale_timestamp) AS sale_date, COUNT(*) AS total_sales
FROM sales
GROUP BY DATE(sale_timestamp)
ORDER BY sale_date;

- Returns the number of sales made on each date ordered by date 

SELECT DATE(sale_timestamp) AS sale_date, COUNT(*) AS total_sales
FROM sales
GROUP BY DATE(sale_timestamp)
ORDER BY sale_date;

- Returns the number of sales made on each date ordered by date (same as the query above)

SELECT * FROM sales
WHERE EXTRACT(HOUR FROM sale_timestamp) < 12;

- Returns the sales made before midday (12 AM) 

SELECT product_name, MIN(sale_timestamp) AS first_sale
FROM sales
GROUP BY product_name;

- Returns the first time each product was sold

SELECT product_name, MAX(sale_timestamp) AS last_sale
FROM sales
GROUP BY product_name;

- Returns the last (most recent) time each product was sold

SELECT DATE(sale_timestamp) AS sale_date, SUM(sale_amount) AS total_sales
FROM sales
WHERE EXTRACT(HOUR FROM sale_timestamp) BETWEEN 12 AND 14
GROUP BY DATE(sale_timestamp);

- Returns the sales made between 12 AM and 2 PM on each date


'''
