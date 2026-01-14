
--Set-2--

--Questions are based on the same database and the same table as in Set-1--

--QUESTIONS and SOLUTIONS:- 

Select * from Employees

--1. How do you select employees who work in the 'IT' department and have a salary greater than 75,000?
Select * from Employees where Department = 'IT' and Salary >75000


--2. How do you find employees who work in the 'HR' department or have a salary less than 60,000?
Select * from Employees where Department='HR' and Salary<60000


--3. How do you select employees who do not work in the 'Finance' department?
Select * from Employees where Department not like 'Finance'

--or
Select * from Employees where Department not in ('Finance')
--or
Select * from Employees where not Department ='Finance'


--4. How do you find employees whose salary is between 60,000 and 70,000 and who work in the 'Finance' department?
Select * from Employees where Department ='Finance' and Salary between 60000 and 70000



--5. How do you find employees who work in the 'IT' department and do not have a salary greater than 80,000?
Select * from Employees where Department ='IT' and Salary<80000


--*6. How do you find employees who work in the 'HR' or 'Finance' departments and have a salary greater than 65,000?
Select * from Employees where (Department ='HR' or Department ='Finance') and Salary >65000


--7. How do you select employees whose last name starts with 'D' and do not work in the 'HR' department?
Select * from Employees where LastName like 'D%' and Department not like 'HR'


--8. How do you find employees who do not work in the 'IT' department and have a salary greater than 70,000?
Select * from Employees where Department not like 'IT'and Salary >70000



--9. How do you select employees who work in the 'IT' department and either have a salary greater 
--than 75,000 or have the first name 'Laura'?

Select * from Employees where (Salary>75000 or FirstName like 'Laura') and Department ='IT'

--10. How do you find employees who do not work in the 'HR' or 'IT' departments?
Select * from Employees where (Department not like 'HR' and Department not like 'IT')

--*or
Select * from Employees where Department not in('HR','IT') --not in HR and IT