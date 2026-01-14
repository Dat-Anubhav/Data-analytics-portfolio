
--FOREIGN KEY Constraint--

/*In SQL, a foreign key is a column (or group of columns) in one table that links to the primary key (or a unique key) of another table. 
It is the primary tool used to establish and enforce relationships between data in different tables, ensuring referential integrity*/

--Case 1: when the new table has to be created

Create table primekey_table(
ID int primary key,
name varchar(256))

--Inserting values
insert into primekey_table
Values(1,'Momoshiki'),(2,'Kayuga'),(3,'Itshiki')

--Checking primarykey table
Select * from primekey_table

--Creating foreign key table
Create table foreignkey_table(
ID int foreign key references primekey_table(ID))

--Forget to add a Course column
Alter table foreignkey_table
add course varchar(256)

--Checking foreignkey_table
Select * from foreignkey_table

--Inserting values
Insert into foreignkey_table
values(1,'Data Science'),(2,'Mathematics'),(3,'AR/VR')

--Checking the table
Select * from foreignkey_table

--Inserting a null value into the foreignkey table
Insert into foreignkey_table
Values(null,'Digital marketing')

--Checking foreignkey_table
Select * from foreignkey_table

--Inserting a value into a foreign key column outside the primary key range
Insert into foreignkey_table
values(6,'Astrophysics')

--As expected it throws an error:- "The INSERT statement conflicted with the FOREIGN KEY constraint "FK__foreignkey_t__ID__5812160E". The conflict occurred in database "Constraints", table "dbo.primekey_table", column 'ID'."
-- This is happening because the foreign key value is not matching any value in the primary key column.
-- A foreign key column can have NULL, but if it has some value, that value must exist in the primary key column.

--Case 2: When the table already exists
Create table foreignkey_table2(
Id int,
course varchar(256))

--Now altering the table
Alter table foreignkey_table2
add foreign key (Id) references primekey_table(ID)

--Inserting values
insert into foreignkey_table2
values(1,'Data analytics'),(2,'Astronomy'),(3,'Biotechnology')

--Checking table
Select * from foreignkey_table2

--Inserting value outside the range of primary key primekey_table
Insert into foreignkey_table2
values(7,'Economics')

--As expected throws an error