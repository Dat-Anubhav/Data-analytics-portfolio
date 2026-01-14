
--Assignment-5--

--View table
Select * from Employees

--Questions and Solutions:- 

--1.) Write a SQL query to select all columns and rows from the Employees table.
Select * from Employees

--2.) Write a SQL query to find the names and email addresses of all employees who work in the department with DepartmentID = 101.
Select FirstName,LastName,Email,DepartmentID from Employees where DepartmentID =101

--3.) Write a SQL query to find the total number of employees in the Employees table.
Select count(EmployeeID) as [Total number of employees] from Employees

--4.) Write a SQL query to find the details of employees who were hired in the year 2020.
Select * from Employees where Year(HireDate)=2020

--5.) Write a SQL query to update the salary of 'Jane Doe' to 90,000.
Update Employees
SET Salary=90000 where FirstName like 'Jane' and LastName like 'Doe'

--Checking Table
Select * from Employees