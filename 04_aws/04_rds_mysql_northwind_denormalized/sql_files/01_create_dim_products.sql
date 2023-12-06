CREATE TABLE IF NOT EXISTS dim_products
SELECT
	ProductID,
	ProductName,
	CategoryName 
FROM db_northwind.Products p
LEFT JOIN db_northwind.Categories c ON p.CategoryID = c.CategoryID;