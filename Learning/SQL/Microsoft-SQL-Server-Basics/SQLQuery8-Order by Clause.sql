
/* ORDER BY clause

The ORDER BY clause in Microsoft SQL Server is used to sort the rows returned by a query. 
It lets you arrange the results in ascending (ASC) or descending (DESC) order based on one or more columns.
​
Basic idea
(i) It comes at the end of a SELECT statement.
(ii) By default, sorting is ascending if you don’t specify ASC or DESC*/

Select * from Employees
order by Salary

--Sorting in Descending order
Select * from Employees
order by Salary Desc

--

-- Sorting employees by HireDate from newest to oldest
Select Firstname,Lastname,HiredDate from Employees
order by HiredDate DESC

--Sorting departments with salary amount
Select Department,Salary from Employees
Order by Salary Desc

--Sorting employees from the EmployeeRecords Table
Select * from EmployeeRecords
order by EmployeeID asc, Salary desc

Select * from EmployeeRecords
order by EmployeeID desc, Salary asc

Select * from EmployeeRecords
order by Salary desc

-- Observation: ORDER BY lets us control how rows are displayed.
-- We can sort by one or more columns (like EmployeeID and Salary),
-- and choose ascending (ASC) or descending (DESC) to get the exact order we want.
