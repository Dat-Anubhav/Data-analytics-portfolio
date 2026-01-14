
--Recursive CTE--

--Finding factorial of a number 5

With [R Cte] as (
Select 1 as n

union all

Select n+1 from [R Cte] where n<=4)

Select exp(sum(log(n))) [Factorial] from [R Cte] 

--As we know log m +log n = log mn
--5! =5*4*3*2*1

--Finding factorial of number 4

with [cte] as (
--Anchor Query
Select 1 as n

union all

--Recursive query
Select n+1 from [cte] where n<=3)

Select exp(sum(log(n))) as [Factorial of 4] from [cte]
