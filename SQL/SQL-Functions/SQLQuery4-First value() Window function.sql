
--First value() Window function--

--Creating table 

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

--VIEW Table
Select * from EmployeeSalaries

--First Value
--Finding Minimum Salary 
Select *,
FIRST_VALUE(Salary) over(order by Salary asc) as [Minumum Salary]
from EmployeeSalaries

--Finding Employee with minimum Salary
 Select*,
 FIRST_VALUE(EmployeeName) OVER (order by Salary asc) as [Employee with Minumum Salary]
 from EmployeeSalaries

--Finding Department with Minimum Salary
Select *,
FIRST_VALUE(Department) over( order by Salary asc) as [Department with Minum Salary]
From EmployeeSalaries

--Finding Maximum pay
Select * from EmployeeSalaries 
where Salary =(Select top 1 FIRST_VALUE(Salary) over(Order by Salary desc) as [Maximum Salary] from EmployeeSalaries)
