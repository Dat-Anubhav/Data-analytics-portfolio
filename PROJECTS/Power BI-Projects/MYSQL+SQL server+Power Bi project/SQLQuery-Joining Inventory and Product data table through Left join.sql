
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

--Creating Production Database
Create database PROD

use PROD

--Importig Production Flat file

--Checking imported data

Select * from [dbo].[Prod+Env+Inventory+Dataset]

Select * from [dbo].[Products+(1)]