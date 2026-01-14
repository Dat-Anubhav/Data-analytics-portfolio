
--Assignment-3--


--VIEW TABLE
Select * from Employees

--Questions and Solutions:-

--1.) Write a SQL query to find the names of employees whose first names start with the letter 'J'.
Select FirstName, LastName from Employees where FirstName like 'J%'

--2.) Write a SQL query to find the names of employees whose last names end with the letter 'n'.
Select FirstName, LastName from Employees where LastName like '%n'

--3.) Write a SQL query to find the email addresses of employees that contain the word "john".
Select Email from Employees where FirstName like 'john'

--4.) Write a SQL query to find the names of employees whose first names have exactly 5 characters.
Select FirstName,LastName from Employees where FirstName like '_____'

--5.) Write a SQL query to find the names of employees whose last names contain the letter 'a' as the second character.
Select FirstName, LastName from Employees where LastName like '%a_'