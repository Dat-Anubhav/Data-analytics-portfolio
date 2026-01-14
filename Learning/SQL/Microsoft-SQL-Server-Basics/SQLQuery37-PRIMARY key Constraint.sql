
--PRIMARY KEY CONSTRAINT--

/*In SQL Server, a Primary Key is a unique identifier for each row in a table, 
ensuring no two records are identical and providing a reliable way to link related data across multiple tables. 
It serves as a combination of a NOT NULL and UNIQUE constraint, 
automatically creating a clustered index to optimize data retrieval.

Conditions for a Primary Key
1.Uniqueness: Every value in the primary key column must be unique; duplicate values are strictly prohibited.
2.No Nulls: The column cannot contain any NULL values; every row must have a valid, non-empty identifier.
3.One Per Table: A table can have only one primary key constraint, though that key can consist of multiple columns (known as a Composite Key).
4.Immutability: Ideally, the values of a primary key should be stable and not change over time, as changing them can break relationships with other tables.
5.Size Limit: In SQL Server 2025, the total length of the columns in a primary key cannot exceed 900 bytes.
*/

--Case 1: When new table has to be created

Create table test_primekey1(
Eid int primary key,
gender char(1),
age tinyint,
firstname varchar(256)
)

insert into test_primekey1
Values(1,'M',23,'Anubhav')

--Inserting same value twice in the Eid column to check Primary key constraint
Insert into test_primekey1
Values(1,'F',22,'Rishu')

--As expected it throws an error:- "Violation of PRIMARY KEY constraint 'PK__test_pri__C1971B536A6A8A7E'. Cannot insert duplicate key in object 'dbo.test_primekey1'. The duplicate key value is (1)."
--because primary key column entries must be unique

--Inserting a null value
insert into test_primekey1
Values(null,'M',28,'Goku')

--As expected it also throws an error:- "Cannot insert the value NULL into column 'Eid', table 'master.dbo.test_primekey1'; column does not allow nulls. INSERT fails."
--because primary key column cannot contain null values 

--Case 2:When table already exists

Alter table test_primekey1
add primary key (age)

--it throws an error : Because a table can have only one primary key

--Creating a new table as test_primekey2

Create table test_primekey2(
Eid int,
gender char(1),
age tinyint,
firstname varchar(256))

insert into test_primekey2
values(1,'F',23,'Ananya')

insert into test_primekey2
values(2,'M',24,'Naman')

Drop table test_primekey2

--creating a new table 
Create table test_primekey3(
Eid int not null unique,
gender char(1),
age tinyint not null unique,
firstname varchar(256))

--altering this table to add a primary key

Alter table test_primekey3
add primary key (age)

--In previous table we were unable to add age column as a primary key because age column lacks NOT NULL and UNIQUE constraints 
--therefore it can have NULL and duplicate values, so sql server was not accepting it as a primary key

--checking as a primary key
Insert into test_primekey3
values(1,'M',25,'Anubhav')

--inserting two same age values
insert into test_primekey3
values(2,'F',25,'Rashmi')

insert into test_primekey3
values(3,'M',25,'Noori')

insert into test_primekey3
values(4,'F',25,'Noori')

--As expected it throws an error and hence age column has successfully converted primary key column

Select * from test_primekey3