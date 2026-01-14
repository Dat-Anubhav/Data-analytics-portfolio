
--INDEXES in MS SQL--

/*An index is a B-Tree data structure that speeds up data retrieval (SELECT) 
but slows down write operations (INSERT, UPDATE) due to maintenance overhead.
Clustered indexes define the physical order of data (one per table), 
while non-clustered indexes are separate pointers to data (multiple per table).*/

Select * from EmployeeRecords

Create index ix_1 on EmployeeRecords(EmployeeID)

Create index ix_2 on EmployeeRecords(FirstName,Salary)

--Creating index in desc order
Create index ix_3 on EmployeeRecords(EmployeeID desc)

--Droping Index ix_1 on EmployeeRecords table
Drop index EmployeeRecords.ix_1







--Main table does not change,because this is a non unique, non- cluster index
