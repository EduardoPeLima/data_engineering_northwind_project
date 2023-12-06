CREATE TABLE IF NOT EXISTS dim_customers
SELECT
	CustomerID,
	CustomerName,
	ContactName,
	Address,
	City,
	PostalCode,
	Country 
FROM db_northwind.Customers c;