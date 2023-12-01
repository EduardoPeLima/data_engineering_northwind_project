CREATE TABLE IF NOT EXISTS OrderDetails
(
    OrderDetailID INT NOT NULL PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
);