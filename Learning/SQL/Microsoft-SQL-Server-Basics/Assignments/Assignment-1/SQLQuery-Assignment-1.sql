
--Assignment-1--

Create Database SQL_Assignments


--Step 1) Create Table
CREATE TABLE EmployeeSales (
    SaleID INT PRIMARY KEY,
    EmployeeID INT,
    Department VARCHAR(50),
    SaleAmount DECIMAL(10, 2),
    SaleDate DATE
);

--Step 2) Insert records into the table
INSERT INTO EmployeeSales (SaleID, EmployeeID, Department, SaleAmount, SaleDate)
VALUES 
(1, 101, 'Electronics', 500.00, '2023-08-01'),
(2, 102, 'Electronics', 300.00, '2023-08-03'),
(3, 101, 'Furniture', 150.00, '2023-08-02'),
(4, 103, 'Electronics', 250.00, '2023-08-04'),
(5, 104, 'Furniture', 200.00, '2023-08-02'),
(6, 101, 'Furniture', 450.00, '2023-08-05'),
(7, 102, 'Electronics', 700.00, '2023-08-05'),
(8, 103, 'Furniture', 100.00, '2023-08-06');


--***********************************************************************************
--Column Definitions
/*
SaleID (INT PRIMARY KEY): Unique identifier for each sale.
EmployeeID (INT): Identifier for the employee who made the sale.
Department (VARCHAR(50)): Name of the department where the sale was made.
SaleAmount (DECIMAL(10, 2)): Total amount of the sale.
SaleDate (DATE): Date when the sale occurred.*/
--***********************************************************************************

--View Table
Select * from EmployeeSales

--Questions:-

--1.) Write a query to calculate the total sales amount for each department in the EmployeeSales table.
Select Department, sum(SaleAmount) as [Total Sale amount] from EmployeeSales
Group by Department

--2.) Write a query to count the number of sales made by each employee.
Select EmployeeID, count(Department) [Number of sales]  from EmployeeSales
Group by EmployeeID

--3.) Write a query to calculate the average sale amount for each department.
Select Department, avg(SaleAmount) [Average Sale Amount] from EmployeeSales
Group by Department

--4.) Write a query to find the total sales amount for each employee, but only include employees who have made more than one sale.
Select EmployeeID, count(Department) [Number of Sales], sum(SaleAmount) [Total Sale Amount] from EmployeeSales
GROUP BY EmployeeID
Having Count(Department)>1 

--5.) Write a query to find the total sales for each month in 2023.
Select Month(SaleDate) as [Month number], sum(SaleAmount) as [Total Sales] from EmployeeSales
Where year(SaleDate)=2023
Group by Month(SaleDate)

