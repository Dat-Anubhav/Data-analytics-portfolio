
--Window functions LEAD and LAG--

--Creating a new database 


create database [Profit DB]

use [profit db]

-- Create a table to store monthly profit data for different products
CREATE  TABLE ProfitData (
    MonthNumber INT,
    MonthName VARCHAR(3),
    Product VARCHAR(50),
    Profit INT
);

-- Insert data into the ProfitData table
INSERT INTO ProfitData (MonthNumber, MonthName, Product, Profit) VALUES
(1, 'Jan', 'Product A', 1000),
(2, 'Feb', 'Product A', 1500),
(3, 'Mar', 'Product A', 1200),
(4, 'Apr', 'Product A', 1700),
(5, 'May', 'Product A', 1300),
(6, 'Jun', 'Product A', 1600),
(1, 'Jan', 'Product B', 2000),
(2, 'Feb', 'Product B', 2500),
(3, 'Mar', 'Product B', 2200),
(4, 'Apr', 'Product B', 2700),
(5, 'May', 'Product B', 2300),
(6, 'Jun', 'Product B', 2600);

--VIEW TABLE
Select * from ProfitData

--LEAD function
Select *,
lead(Profit) over(order by MonthNumber) as [Lead profit]
from ProfitData

Select *,
lead(Profit) over(Partition by Product order by MonthNumber) as [Next profit]
from ProfitData

--LAG function

Select *,
lag(Profit) over(order by MonthNumber) as [Previous profit]
from ProfitData

Select *,
lag(Product) over(Order by MonthNumber) as [previous product]
from ProfitData

-- I want only MonthName,Product,Profit column
Select MonthName,Product,Profit,
lead(Profit) over(order by MonthNumber) as [Lead  profit]
from ProfitData

Select MonthNumber,MonthName,Profit,
Lead(sum(Profit)) over(Order by MonthNumber) as [Lead profit]
from ProfitData
Group by MonthNumber,MonthName,Profit
order by MonthNumber

--When using aggregation functions like SUM(), every non-aggregated column in your SELECT list must appear in the GROUP BY clause
--
Select MonthNumber,MonthName,Profit,
Lead(Profit) over(Order by MonthNumber) as [Lead profit]
from ProfitData
Group by MonthNumber,MonthName,Profit
order by MonthNumber


Select * from ProfitData