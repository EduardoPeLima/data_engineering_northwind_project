CREATE TABLE IF NOT EXISTS dim_suppliers
SELECT
	SupplierID,
	SupplierName,
	ContactName,
	Address,
	City,
	PostalCode,
	Country,
	Phone
FROM db_northwind.Suppliers s