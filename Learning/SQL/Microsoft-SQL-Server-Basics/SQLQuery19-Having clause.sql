
--HAVING clause--

--Total Sales, Avg Sales, Total Quantity, Avg Quantity for each distinct product
select 
ProductID,
sum(Quantity) as [Total Quantity],
sum(TotalAmount) as [Sum of Amount],
avg(Quantity) [Average Quantity Sold],
avg(TotalAmount) [Average Amount]
from dbo.Sales
group by ProductID
Having sum(TotalAmount)<700 and sum(Quantity)<26 -- Finding ProductID having totaL amount <700 and total Quantity<26 
