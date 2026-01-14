
--Like Operator--

--Creating new table to practice like operator


-- Create Employees_us table
CREATE TABLE Employees_US (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50)
);

-- Insert sample data into Employees table
INSERT INTO Employees_us (EmployeeID, FirstName, LastName, Department) VALUES
(1, 'Alice', 'Smith', 'Finance'),
(2, 'Bob', 'Johnson', 'Engineering'),
(3, 'Charlie', 'Williams', 'Marketing'),
(4, 'Diana', 'Brown', 'Finance'),
(5, 'Edward', 'Jones', 'Engineering'),
(6, 'Fiona', 'Garcia', 'Marketing'),
(7, 'George', 'Miller', 'Finance'),
(8, 'Hannah', 'Wilson', 'Engineering');



--1) Find Employees whose Last Name starts with 'S'.
Select * from Employees_US where LastName like 's%' 

--2) Find Employees whose First Name ends with 'a'.
Select * from Employees_US where FirstName like '%a'


--3) Find Employees whose Department contains 'Eng'.
Select * from Employees_US where Department like 'Eng%'

--%Eng% will give any where in the start,middle or at the end
Select * from Employees_US where Department like '%Eng%'

--4) Find Employees whose Last Name is exactly 5 characters long.
Select * from Employees_US where LastName like '_____'

--5) Find Employees whose First Name starts with 'C' or 'D'.
Select * from Employees_US where FirstName like '[CD]%'

--6) Find Employees whose Last Name contains 'son'.
Select * from Employees_US  where LastName like '%son%'


--7) Find Employees whose First Name contains the letter 'i' as the second character.
Select * from Employees_US where FirstName like '_i%'

--8) Find Employees whose Last Name starts with any letter between 'A' and 'L'.
Select * from Employees_US where LastName like '[a-l]%'

--9) Find Employees whose First Name does not contain 'o'.
Select * from Employees_US where FirstName not like '%o%'

--10) Find Employees whose Last Name ends with 'a' and is exactly 5 characters long.
Select * from Employees_US where LastName like '____a'

--11) Find Employees whose Department starts with 'Mar' and ends with 'ing'.
Select * from Employees_US where Department like 'mar%ing'

--12) Find Employees whose First Name has an 'a' in the third position.
Select * from Employees_US where FirstName like '__a%'

--13) Find Employees whose Last Name starts with 'Br' or 'Bl'.
Select * from Employees_US where LastName LIKE '[BrBl]%'

--Same thing can also be written as 
Select * from Employees_US where LastName like 'Br%' or LastName like 'Bl%'

--14) Find Employees whose First Name starts with a vowel.
Select * from Employees_US where FirstName like '[aeiou]%'

--15) Find Employees whose First Name does not start with a consonant.
Select * from Employees_US where FirstName not like '[^aeiou]%' --In a SQL Server LIKE pattern, the ^ inside square brackets means “NOT these characters.”

--16) Find Employees whose First Name starts with a consonant.
Select * from Employees_US where FirstName like '[^aeiou]%'