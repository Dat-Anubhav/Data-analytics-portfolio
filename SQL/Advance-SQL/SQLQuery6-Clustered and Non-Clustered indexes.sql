
--Clustered Index--

--Creating new database to test index

Create database Test_Index

use Test_Index

--Creating table
create table Students ( id int, name nvarchar(50), age int, gender varchar(20))

insert into Students values
(1,'Raj',23,'M'),
(4,'Nitin',25,'M'),
(3,'Priya',21,'F'),
(2,'Nikita',20,'F'),
(5,'Monica',20,'F')

--Checking table
Select * from Students

--Creating clustered Index
Create clustered index C_ix_1 on Students(id)

Create clustered index C_ix_2 on Students(gender desc,age asc)

--As expected It shows an error

--Note:-There can be only one clustered index in a table at a time

--Droping Clustered index C_ix_1
Drop index Students.C_ix_1

--Creating new index with 2 columns combine one in desc other one in asc
Create Clustered index C_ix_2 on Students(gender desc,age asc)

--Checking the main table
Select * from Students

---------------------------------------------

--NON-CLUSTERED Index--

--Creating a non-clustered index
Create nonclustered index nc_ix_1 on Students(id)

--Creating Non-clustered index with 2 columns combine one in desc another one in asc
Create nonclustered index nc_ix_2 on Students(age desc,gender asc)

--Checking table
Select * from Students





--As we can see non cluster do not make changes in the main table, 
--because they are seperate pointer to data and there can be multiple non clustered index on a table
