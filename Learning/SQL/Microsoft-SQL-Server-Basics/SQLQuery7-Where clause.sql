
--Where clause

Select * from EmployeeRecords
where EmployeeID=5

Select * from [dbo].[EmployeeRecords]
where EmployeeID=2

Select Firstname,Salary from EmployeeRecords
where EmployeeID=4

-- Checking if any employee has a salary greater than 95000
Select Firstname,Salary from EmployeeRecords where Salary>95000

-- Checking if any employee has a salary less than 95000
Select Firstname,Lastname,Salary from EmployeeRecords
where Salary<95000

Select * from EmployeeRecords

-- Finding employees who are in the Marketing department
Select * from EmployeeRecords where Department='Marketing'