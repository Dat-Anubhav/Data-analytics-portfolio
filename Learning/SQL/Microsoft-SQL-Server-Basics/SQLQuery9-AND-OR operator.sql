
--AND/OR operator

Select * from Employees
Where Department='Marketing' and EmployeeID=4

Select * from EmployeeRecords
where Firstname='Anubhav' or Firstname='Rishu'

Select * from EmployeeRecords
where (Firstname='Anubhav' or Firstname='Rishu') and Department = 'Data Science'