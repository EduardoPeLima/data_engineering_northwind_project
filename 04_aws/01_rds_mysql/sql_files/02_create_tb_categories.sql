CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(255),
    Description VARCHAR(255),
    dt_extract_data DATETIME,
    na_file_name VARCHAR(80)
);