
use Our_employee_details

Select * from INFORMATION_SCHEMA.COLUMNS
where table_name='EmployeeRecords'

--NULL, IS NULL, IS NOT NULL

Select * from EmployeeRecords Where department = null

Select * from EmployeeRecords Where Salary is null

Select * from EmployeeRecords

Select * from EmployeeRecords Where Salary is not null

Select distinct Firstname from EmployeeRecords