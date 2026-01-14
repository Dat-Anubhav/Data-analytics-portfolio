
--COMMON TABLE EXPRESSION(C.T.E)--

/*
A Common Table Expression (CTE) in SQL is a temporary result set that you can reference within a 
SELECT, INSERT, UPDATE, or DELETE statement. CTEs are defined using the WITH keyword, 
and they can make complex queries easier to write, understand, and maintain by breaking them into simpler parts.
*/
Select * into #temp3 from EmployeeRecords
Select * into #temp4 from [dbo].[EmployeeRecords]

--CTE Table syntax

With cte1 as(
Select * from #temp1
)

Select * from cte1 

--Example 1 : Update

With Cte2 as(
Select * from #temp3 where EmployeeID in (4,5,6))

Update #temp3 Set EmployeeID=10 where EmployeeID in (Select distinct EmployeeID from Cte2) 

Select * from #temp3

--Example 2 : Delete

With Cte3 as(
Select * from #temp4 where EmployeeID =4
)
Delete from #temp4 where EmployeeID in (Select distinct EmployeeID from Cte3)

Select * from #temp4

--Example 3: Insert
Select * into #temp5 from EmployeeRecords

With CTE4 as(
Select * from #temp5 where EmployeeID =5)

Insert into #temp4 Select * from CTE4

Select * from #temp4

--------------------------------

--Nested CTE

--Example 1:
WIth CTE1 as(
Select * from #temp3),CTE2 as(Select * from #temp4)

Select * from CTE1
union all
Select * from CTE2

--Example 2 :
WIth CTE3 AS (
Select FirstName,Lastname from #temp3 where Department like 'IT'),CTE5 as (Select EmployeeID, Department from #temp4 where Department like 'IT' )

Select * from CTE3
UNION ALL
Select * from CTE5