CREATE TABLE IF NOT EXISTS fact_orders
SELECT
	o.OrderID,
	o.CustomerID,
	o.EmployeeID,
	o.OrderDate,
	o.ShipperID,
	od.ProductID,
	od.Quantity,
	p.Price,
	p.SupplierID
FROM db_northwind.Orders o
left join db_northwind.Orderdetails od on o.OrderID = od.OrderID 
left join db_northwind.Products p on od.ProductID = p.ProductID;