CREATE TABLE IF NOT EXISTS Employees
(
    EmployeeID INT PRIMARY KEY,
    LastName VARCHAR(255),
    FirstName VARCHAR(255),
    BirthDate DATE,
    Photo VARCHAR(255),
    Notes TEXT,
    dt_extract_data DATETIME,
    na_file_name VARCHAR(80)
);