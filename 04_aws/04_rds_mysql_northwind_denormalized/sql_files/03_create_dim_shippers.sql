CREATE TABLE IF NOT EXISTS dim_shippers
SELECT
	ShipperID,
	ShipperName,
	Phone
FROM db_northwind.Shippers s 