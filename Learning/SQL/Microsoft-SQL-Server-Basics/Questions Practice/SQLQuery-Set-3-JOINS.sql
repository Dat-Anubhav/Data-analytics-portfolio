
--SET-3-JOINS--

--Creating new database
create database [SQL Questions]

use [SQL Questions]

-- Create the Customers table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    Country VARCHAR(50)
);

-- Insert data into Customers table
INSERT INTO Customers (CustomerID, CustomerName, Country)
VALUES 
(1, 'Alice', 'USA'),
(2, 'Bob', 'UK'),
(3, 'Charlie', 'Canada'),
(4, 'David', 'USA'),
(5, 'Eve', 'Australia');

-- Create the Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    ProductID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Insert data into Orders table
INSERT INTO Orders (OrderID, CustomerID, OrderDate, ProductID)
VALUES 
(101, 1, '2024-08-01', 1001),
(102, 1, '2024-08-03', 1002),
(103, 2, '2024-08-04', 1001),
(104, 3, '2024-08-05', 1003),
(105, 5, '2024-08-06', 1004);

-- Create the Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10, 2)
);

-- Insert data into Products table
INSERT INTO Products (ProductID, ProductName, Price)
VALUES 
(1001, 'Laptop', 1000),
(1002, 'Smartphone', 700),
(1003, 'Tablet', 500),
(1004, 'Headphones', 200),
(1005, 'Smartwatch', 300);

--TABLES:-


select * from Customers

select * from Orders

select * from Products



--Questions and Solutions:-


--1) Write an SQL query to find the names of customers who have placed an order.
Select c.CustomerID,c.CustomerName,c.Country,o.OrderDate, o.OrderID,o.ProductID from Customers c inner join Orders o on c.CustomerID=o.CustomerID

--2) Find the list of customers who have not placed any orders.
Select c.CustomerID,c.CustomerName,c.Country,o.OrderDate, o.OrderID,o.ProductID from Customers c left join Orders o on c.CustomerID=o.CustomerID
where o.OrderID is null

--3) List all orders along with the product name and price.
Select o.OrderID,o.ProductID,p.ProductName,p.Price from Orders o join Products p on o.ProductID=p.ProductID

--With distintct product name
Select distinct ProductName,Price from Orders o join Products p on o.ProductID= p.ProductID 

--Why to use join?
Select distinct ProductName,Price from Products --we use join because one Product (Smartwatch did not have an orderId, means never ordered by any customer) 

--4) Find the names of customers and their orders, including customers who haven't placed any orders.
Select CustomerName,OrderID from Customers c left join Orders o on c.CustomerID=o.CustomerID 

--5) Retrieve a list of products that have never been ordered.
Select ProductName,OrderID from Orders o right join Products p on o.ProductID=p.ProductID where OrderID IS NULL

--6) Find the total number of orders placed by each customer.
Select CustomerID,Count(OrderID) as [No. of orders] from Orders
Group by CustomerID

--Or 
--Performing join to get Customer name
Select CustomerName,Count(OrderID) as [No. of Orders] from Customers c join Orders o on c.CustomerID=o.CustomerID 
Group by CustomerName

--OR 
--This will give all customer's names, including those who haven't placed any orders (Left join)
Select CustomerName,Count(OrderID) as [No. of Orders] from Customers c Left join Orders o on c.CustomerID=o.CustomerID 
Group by CustomerName

--7) Display the customers, the products they've ordered, and the order date. Include customers who haven't placed any orders.
Select c.CustomerName,p.ProductName,o.OrderDate from Customers c left join Orders o on c.CustomerID=o.CustomerID left join Products p on o.ProductID=p.ProductID




