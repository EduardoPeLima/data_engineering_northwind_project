CREATE TABLE IF NOT EXISTS Suppliers
(
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255),
    ContactName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(255),
    PostalCode VARCHAR(20),
    Country VARCHAR(255),
    Phone VARCHAR(20),
    dt_extract_data DATETIME,
    na_file_name VARCHAR(80)
);