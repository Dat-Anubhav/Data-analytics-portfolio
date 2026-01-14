
--UNIQUE CONSTRAINT--
--It ensures that a column consists of unique values

--Case 1: We need to create a table
Create table test_unique1(
Sid int unique,
age tinyint not null,
firstname varchar(256) not null unique,
lastname varchar(256));

Select * from test_unique1

--Inserting two same Sid
insert into test_unique1
values(1,24,'Anubhav','Srivastav')

insert into test_unique1
values(1,23,'Rishu','Srivastav')
 
--As expected it throws an error:- Violation of UNIQUE KEY constraint 'UQ__test_uni__CA1E5D79C10E7E23'. Cannot insert duplicate key in object 'dbo.test_unique1'. The duplicate key value is (1)

--case 2:- when the table already exists
--altering age column into unique and nullable

alter table test_unique1
add unique (age)

Select * from test_unique1

--INSERTING two same values in age column
insert into test_unique1
values(2,30,'Harry','Potter')

insert into test_unique1
values(3,30,'Neji','Huga')

--As expected this also throws an error