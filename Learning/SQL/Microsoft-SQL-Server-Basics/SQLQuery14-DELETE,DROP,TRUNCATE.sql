
--DELETE, TRUNCATE, Drop

use Our_employee_details

--Creating temporary tables for practicing Delete,Truncate and Drop
Select * Into #1 from EmployeeRecords

Select * from #1

--DELETE

--Deleting row where there is null values
Delete from #1 where Firstname is null

--Checking Temporay table #1
Select * from #1

--Truncate
--Deleting entire table #1 

Truncate table #1

--Checking Temporary table #1
Select * from #1

--DROP

--Creating table #2
Select * Into #table2 from EmployeeRecords

Select * from #table2

Drop table #table2

--Checking table #2
Select * from #table2

--Delete - delete certain records from the table

--if we will use delete without where condition, all records from the table will be deleted, but the 
--table structure remains intact

--Truncate - delete all the records from the table but the structure of the table remains intact

--Drop - all the records will be deleted plus table structure will also be removed