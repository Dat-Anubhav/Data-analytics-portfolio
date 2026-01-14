
--Max function--

Select max(Salary) from EmployeeRecords

--Defining name for the max(Salary) column
Select max(Salary) as [MAX_SALARY] from EmployeeRecords

Select * from EmployeeRecords

--Group By--

--Finding Department with maximum salary
Select Department,max(Salary) as [max_pay]from EmployeeRecords
Group by Department

--Min function--

--Finding Department with minimum Salary
Select Department,min(Salary)as [min_pay] from EmployeeRecords
group by Department
