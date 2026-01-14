
--Set-4-Joins--

--TABLES

Select * from Customers
Select * from Orders
Select * from Products

--Questions and Solutions:-

--1.) Indentify the pairs of customers who live in the same country
Select * from Customers x join Customers y on x.Country=y.Country and x.CustomerID <> y.CustomerID and x.CustomerID>y.CustomerID--u can write y.CustomerID>x.CustomerID it works both ways

/* 
* <> means not equal to
* x.CustomerID <> y.CustomerID:- it remove's the rows which have same CustomerID(Output) and keep only which have different CustomerID
*/

--2.) Find the Customer who has spent the most on their orders
Select c.CustomerName, sum(Price) as [Amount spent] from Customers c join Orders o on c.CustomerID=o.CustomerID join Products p on o.ProductID=p.ProductID
Group by CustomerName

--3.)