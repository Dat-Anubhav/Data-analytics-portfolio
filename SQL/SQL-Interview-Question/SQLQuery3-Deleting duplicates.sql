
--Deleting duplicates--

Select * from EmployeeRecords

--Taking backup
Select * into emprec_bkp from EmployeeRecords

--Checking table
Select * from emprec_bkp

--Deleting duplicates employeeid

Select distinct * into #1 from emprec_bkp

--truncating emprec_bkp
truncate table emprec_bkp

--Filling distinct values in emprec_bkp
insert into emprec_bkp Select * from #1

--Modified table
Select * from emprec_bkp

--deleting null record
delete from emprec_bkp where FirstName is null

--Checking table
Select * from emprec_bkp

------------------------------------
--Method 2 using CTE sn row_number

--taking backup of the employeerecords table
Select * into emprec_bkp2 from EmployeeRecords

--View table
Select * from emprec_bkp2

with cte as (
Select *, row_number() over(Partition by FirstName order by EmployeeID) [row number] from emprec_bkp2)

--Select * from cte

delete from cte where [row number]>1

--Check table emprec_bkp2
Select * from emprec_bkp2

--removing null value
delete from emprec_bkp2 where Firstname is null

--Checking table
Select * from emprec_bkp2
