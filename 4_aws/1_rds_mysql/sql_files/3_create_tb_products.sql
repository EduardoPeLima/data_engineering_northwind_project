CREATE TABLE IF NOT EXISTS Products
(
    ProductID INT NOT NULL PRIMARY KEY,
    ProductName VARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(255),
    Price DECIMAL(10, 2) DEFAULT 0,
    FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers (SupplierID)
);
