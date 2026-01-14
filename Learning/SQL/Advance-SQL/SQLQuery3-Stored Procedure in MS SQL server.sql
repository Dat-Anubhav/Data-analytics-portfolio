
--Stored Procedures in MS Sql server--

--Syntax:-

Create procedure sp_test_1
as
begin
Select * from EmployeeRecords
end

execute sp_test_1

--Example2:

Create proc sp_test_2 --Procedure can also be written as proc
as
begin
Select FirstName, Salary from EmployeeRecords
end

sp_test_2

--Altering stored procedure

Alter proc Sp_test_2
as
begin
Select FirstName,LastName,Salary from EmployeeRecords
end

sp_test_2