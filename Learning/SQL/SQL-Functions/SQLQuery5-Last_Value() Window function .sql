
--Last_Value() Window Function--

--Creating Table

CREATE TABLE EmployeeSalaries2 (
    EmployeeID INT,
    EmployeeName VARCHAR(50),
    Salary INT,
    Department VARCHAR(50)
);


INSERT INTO EmployeeSalaries2 (EmployeeID, EmployeeName, Salary, Department)
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

--View Table:-
Select * from EmployeeSalaries2

--Incorrect query:-
Select *,
Last_value(Salary) over(Order by Salary) [Maximum Salary] 
from EmployeeSalaries2-- Giving Same value as in the respective row

--Correct Query:-
Select *,
LAST_VALUE(Salary) over(Order by Salary asc rows between Unbounded preceding and unbounded following) [Maximum Salary]
from EmployeeSalaries2

--Finding Maximum Salary by Department
Select *,
Last_value(Salary) over(Partition by Department Order by Salary asc rows between unbounded preceding and unbounded following) as [Maximum Salry in the Department]
from EmployeeSalaries2

--Finding Maximum Paid Department
Select *,
LAST_VALUE(Department) over(Order by Salary asc rows between Unbounded preceding and unbounded following) as [Maximum Paid Department]
from EmployeeSalaries2

--Finding Employee with Mamimum Salary
Select *,
LAST_VALUE(EmployeeName) over(Order by Salary rows between unbounded preceding and unbounded following) as [Maximum Paid Employee]
from EmployeeSalaries2

--Why to Use Last value() instead of First_Value() with desc Order by?

/*
LAST_VALUE() is more efficient because it reuses your existing sort order instead of forcing the computer to re-sort the entire dataset in reverse.
It allows you to find the "latest" value while keeping a natural chronological timeline, which makes your code much easier for others to read and understand.
It is more powerful for "running updates" and handling empty values (NULLs) within a specific sequence without breaking the logic of your query.
*/

--Why does this mean " rows between unbounded preceding and unbounded following"

/*
It tells the computer to look at the entire list (from the very first row to the very last row) instead of stopping at your current row.
Without this, LAST_VALUE() only sees up to where you are currently reading, which would incorrectly return your current row as the "last" one.
*/