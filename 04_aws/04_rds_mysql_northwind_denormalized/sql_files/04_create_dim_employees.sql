CREATE TABLE IF NOT EXISTS dim_employees
SELECT
	EmployeeID,
	LastName,
	FirstName,
	BirthDate
FROM db_northwind.Employees e;