
--Practicing to select Distincts--

Select * from EmployeeRecords

Select distinct Firstname from EmployeeRecords

Select distinct Firstname,Lastname from EmployeeRecords

Select distinct Salary from EmployeeRecords

Select distinct * from EmployeeRecords 
/*This returns the same rows as SELECT * here, because no two rows in EmployeeRecords 
are completely identical (EmployeeID is unique)/*