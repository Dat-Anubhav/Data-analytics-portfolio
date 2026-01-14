
--Copying data from one table to another--

--Case 1 : The New table simply doesn't exist
--Case 2: The New table structure/New Table exists

--Case 1:- 

Select * into New_table1 from Products

Select * from New_table1

--Droping the table to experiment for copying only one column 
Drop table  New_table1

--Copying productID into New_table1
Select ProductID into New_table1 from Products

--Checking the New_table1
Select * from New_table1

Truncate table New_table1

--Checking status of the table
Select * from New_table1

--Case 2:- 

Select top 0 * into New_table2 from Products

Insert into New_table2 Select * from Products

--Checking the New_table2
	Select * from New_table2

--Method 2 to create a holow structure replica of Product table

Select * into New_table3 from Products where 1=0

--Checking New_table3
Select * from New_table3

insert into New_table3 Select * from Products 

--Checking New_table3 status
Select * from New_table3
