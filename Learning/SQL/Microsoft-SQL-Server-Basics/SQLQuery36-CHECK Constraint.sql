
--CHECK CONSTRAINTS--
--It checks for certain condition that can be applied on the columns of a table, if this condition is not
--fulfilled, we will not be able to insert the records into the table

--Case 1 :- Table doesn't exist

Create table Test_check(
Eid int ,
firstname varchar(256),
age tinyint check(age>=10));

Insert into Test_check
Values(1,'Anubhav',25)

--Checking Test_check status
Select * from Test_check 

--Inserting age value less than 10
insert into Test_check values(2,'Rishu',6)

--A expected it throws an error :- "The INSERT statement conflicted with the CHECK constraint "CK__Test_check__age__6B24EA82". The conflict occurred in database "Our_employee_details", table "dbo.Test_check", column 'age'."
--We receive an error when an age value less than 10 is entered due to the check "age >= 10".

--Case 2: if the table already exists
--altering EId colum n placing check of greater than 11
alter table Test_check
add check (Eid>11)

--Updating	Eid as it already consistanentry less than 11
update Test_check set Eid=12 where Eid=1

--Checking Test_check table
Select * from Test_check

--Now altering the Eid column and placing a check greater than 11
Alter table Test_check
add check (Eid>11)

--now entering a value
insert into Test_check values(12,'Saitama',22) 

--Checking Test_check
Select* from Test_check

--Now inserting an Eid value less than 11

insert into Test_check values(3,'Genos',55)
--As expected it throws an error of our check constraint check(Eid>11)