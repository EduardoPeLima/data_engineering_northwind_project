CREATE TABLE IF NOT EXISTS Customers
(
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    ContactName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(255),
    PostalCode VARCHAR(20),
    Country VARCHAR(255),
    dt_extract_data DATETIME,
    na_file_name VARCHAR(80)
);