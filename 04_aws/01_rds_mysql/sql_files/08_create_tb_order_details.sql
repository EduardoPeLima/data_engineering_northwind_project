CREATE TABLE IF NOT EXISTS OrderDetails
(
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID),
    dt_extract_data DATETIME,
    na_file_name VARCHAR(80)
);