
Select * from Sales

--Count--

Select COUNT(*) FROM Sales

--Defining column name

Select count(*) as [No.of rows] from Sales

--Counting Quantity

select count(Quantity) as [Quantity] from Sales

--Counting Distinct Payment methods

Select count(PaymentMethod) as [PaymentMethod] from Sales

--Group by payment methods to get no of payments from each payment category
Select PaymentMethod, count(PaymentMethod) as [payment methods] from Sales
Group by PaymentMethod

Select PaymentMethod, count(*) as [Pay mode] from Sales
Group by PaymentMethod

/*COUNT(column) skips NULLs, but COUNT(*) counts all rows (including rows where the column is NULL),
so results can differ when the column contains NULL values.*/

Select * from Sales

--Finding Total sale amount, mode of payment for each Product
Select ProductID,PaymentMethod, sum(TotalAmount) as [Total sale amount] from Sales
Group by ProductID,PaymentMethod
Order by ProductID