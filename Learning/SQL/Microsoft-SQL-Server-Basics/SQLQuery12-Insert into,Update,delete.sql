
--INSERT INTO
use Our_employee_details

Select * from EmployeeRecords
 
INSERT INTO EmployeeRecords(EmployeeID,Firstname,Lastname,Department,Salary)
values
(9,'Hashirama','Senzu','IT',130234.45)

Select * from EmployeeRecords

--Filling NULL entries in row 8

Update EmployeeRecords
Set
Firstname='Bruce',
Lastname='Banner',
Department='Marketing',
Salary=150000
where EmployeeID=8

--Checking Database

Select * from EmployeeRecords

--Deleting the row 10

Delete from EmployeeRecords where Firstname='Tony'

--Checking Database
Select * from EmployeeRecords


