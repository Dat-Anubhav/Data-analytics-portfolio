
--Creating new database
Create database test_env

use test_env

--Importing flat files

--Checking imported data 

Select * from [dbo].[Test+Environment+Inventory+Dataset]

select * from [dbo].[Products]

Select distinct [Demand] from [dbo].[Test+Environment+Inventory+Dataset]

--Applying Left join on Inventory and Product table

Select a.Order_Date_DD_MM_YYYY,a.Product_ID,a.Availability,a.Demand,b.Product_Name,b.Unit_Price 
from [dbo].[Test+Environment+Inventory+Dataset] as a Left join [dbo].[Products] as b on a.Product_ID=b.Product_ID

--------------------------------------------------------------
--Storing LEFT JOIN data table into a new table
Select * into New_table from 
(
Select a.Order_Date_DD_MM_YYYY,a.Product_ID,a.Availability,a.Demand,b.Product_Name,b.Unit_Price 
from [dbo].[Test+Environment+Inventory+Dataset] as a Left join [dbo].[Products] as b on a.Product_ID=b.Product_ID
)x

--Checking New_table
Select * from New_table

--Next step is to import this New_table data into Power Bi

--------------------------------------------------------------
--Creating Production Database
Create database PROD

use PROD

--Importig Production Flat file

--Checking imported data

Select * from [dbo].[Prod+Env+Inventory+Dataset]

Select * from [dbo].[Products+(1)]

--Checking for null Values

Select Distinct [Order_Date_DD_MM_YYYY] from[dbo].[Prod+Env+Inventory+Dataset]
where Order_Date_DD_MM_YYYY is null or Order_Date_DD_MM_YYYY = ''

Select * from [dbo].[Prod+Env+Inventory+Dataset] order by Product_ID

--Incorrect data 
--Product Id 21 is actually Product ID 7
--Product id 22 is actually Product ID 11

--Updating values
Update [dbo].[Prod+Env+Inventory+Dataset]
set Product_ID = 7 where Product_ID = 21

Update [Prod+Env+Inventory+Dataset]
Set Product_ID = 11 where Product_ID = 22

--Checking data
Select Distinct Product_ID from [Prod+Env+Inventory+Dataset] order by Product_ID desc


--Checking for null values
Select distinct [Availability] from [dbo].[Prod+Env+Inventory+Dataset]

--A s we can see no null values

--Checking for Demand column
Select distinct [Demand] from [dbo].[Prod+Env+Inventory+Dataset]

--Now applying a LEFT join as done in the test environment, 
--but this time in the production database with the production dataset.

--Storing LEFT JOIN data table into a new table
Select * into New_table from 
(
Select a.Order_Date_DD_MM_YYYY,a.Product_ID,a.Availability,a.Demand,b.Product_Name,b.Unit_Price 
from [dbo].[Prod+Env+Inventory+Dataset] as a Left join [dbo].[Products+(1)] as b on a.Product_ID=b.Product_ID
)x

--Checking New_table
Select * from New_table

--Next step is Shift Power Bi reports from Test environment database to Production environment database