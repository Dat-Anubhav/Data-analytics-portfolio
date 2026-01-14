
--NULL CONSTRAINT--

--Creating new Database
Create Database Constraints

use Constraints

--Constraints 
--Conditions that can be applied on columns of a table & these conditions are to be followed while
--inserting records into the table

--NOT NULL CONSTRAINT

--Case 1:- We have to create a new table

Create table test_not_null(
Eid int not null,
age tinyint,
firstname varchar(256));

--Checking status of the table test_not_null
Select * from test_not_null

Select * from INFORMATION_SCHEMA.columns where TABLE_NAME like 'test_not_null'

Insert into test_not_null
values(1,23,'Rishu')

--But if we give null value in the Eid column then
insert into test_not_null
values(null,24,'Anubhav')

--As expected it throws an error:- Cannot insert the value NULL into column 'Eid', table 'Constraints.dbo.test_not_null'; column does not allow nulls. INSERT fails. 

--Case 2 : the table already exists
--We want to make Firstname column not null

Alter table test_not_null
alter column firstname varchar(256) not null

--Now checking by giving null value in the firstname column
insert into test_not_null
values(3,28,null)

--As expected it throws an error :- Cannot insert the value NULL into column 'firstname', table 'Constraints.dbo.test_not_null'; column does not allow nulls. INSERT fails.

--Making age column nullable
Alter table test_not_null
alter column age tinyint null

--Inserting null value
insert into test_not_null
values(4,null,'ayush')

--Checking status of the table 
Select * from test_not_null