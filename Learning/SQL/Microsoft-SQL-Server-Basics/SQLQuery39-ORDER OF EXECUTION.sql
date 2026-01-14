
--ORDER OF EXECUTION--

--Creating a new table

CREATE TABLE EmployeeSalaries (
    EmployeeID INT,
    EmployeeName VARCHAR(50),
    Salary INT,
    Department VARCHAR(50)
);


INSERT INTO EmployeeSalaries (EmployeeID, EmployeeName, Salary, Department)
VALUES
(1, 'Alice', 50000, 'HR'),
(2, 'Bob', 60000, 'HR'),
(3, 'Charlie', 55000, 'HR'),
(4, 'David', 75000, 'Finance'),
(5, 'Eve', 80000, 'Finance'),
(6, 'Frank', 72000, 'Finance'),
(7, 'Grace', 90000, 'IT'),
(8, 'Heidi', 95000, 'IT'),
(9, 'Ivan', 87000, 'IT');

--Checking Table
Select * from EmployeeSalaries

--Correct Query
Select distinct top 1 Department, Avg(Salary) as [Average Salary] 
from EmployeeSalaries
where Salary>50000
group by Department
Having avg(Salary)>55000
order by Department asc

--Order of execution:-

--From & Joins :- 1st 
--where         :- 2nd
--group by      :- and so on
--having
--select
--distinct
--order by
--top

--Incorrect Query

select distinct top 1 Department,AVG(Salary) [Avg Salary] 
from EmployeeSalaries
where Salary>50000
group by Department
having [Average Salary]>55000
order by Department 

--As expected it throws an error:- "Invalid column name 'Avg Salary'."
--Because in order of execution having clause is executed first then select, distinct and all, therefore it shows Invalid column name 'Average Salary'