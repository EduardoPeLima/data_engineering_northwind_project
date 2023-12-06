CREATE TABLE IF NOT EXISTS Shippers
(
    ShipperID INT PRIMARY KEY,
    ShipperName VARCHAR(255),
    Phone VARCHAR(20),
    dt_extract_data DATETIME,
    na_file_name VARCHAR(80)
);