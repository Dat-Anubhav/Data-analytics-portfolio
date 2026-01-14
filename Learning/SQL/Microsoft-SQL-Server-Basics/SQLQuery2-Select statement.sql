
-- Practicing to Select statement

use Our_employee_details

Select * From Employees

Select Firstname from Employees

Select Firstname,Lastname from Employees

Select Firstname,lastname,Salary from Employees

Select EmployeeID, Concat(Firstname,' ',Lastname) from Employees

Select EmployeeId, Concat(Firstname,' ',Lastname) as [Employee_Name] from Employees