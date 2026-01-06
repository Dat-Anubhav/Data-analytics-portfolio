
--Finding Nth Highest Salary--

--Finding 2nd highest Salary
Select max(Salary) as [2nd Highest Salary] from EmployeeRecords where Salary<(Select max(Salary) from EmployeeRecords)

--Finding 3rd Highest Salary
Select max(Salary) as [3rd Highest Salary] from EmployeeRecords 
where Salary<(Select max(Salary) from EmployeeRecords 
where Salary<(Select max(Salary) from EmployeeRecords))

--Finding Nth Highest Salary Using CTE and Dense rank
With Cte1 as(Select *,Dense_Rank() over(order by Salary desc) [DR] from EmployeeRecords)

Select Salary from Cte1 where DR=3--DR=Nth number

--Using Sub-Query and Dense rank
Select Salary as [Nth Highest Salary] from (Select *, Dense_Rank() over(order by Salary desc) [DR] from EmployeeRecords) x --Always remember to give a name to these subquery
where DR=2

--All details of a person with 2nd Highest Salary
Select * from (Select *, Dense_Rank() over(order by Salary desc) [DR] from EmployeeRecords) x 
where DR=2



