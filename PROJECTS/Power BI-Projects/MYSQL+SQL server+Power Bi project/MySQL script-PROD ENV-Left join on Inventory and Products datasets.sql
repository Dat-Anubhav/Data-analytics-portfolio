
Use PROD;

/*importing Production dataset*/

/*Checking imported data*/
Select * from PROD.`prod+env+inventory+dataset`;

/*Incorrect data 
Product Id 21 is actually Product ID 7
Product id 22 is actually Product ID 11

Updating values*/

Update PROD.`prod+env+inventory+dataset`
set `Product ID` = 7 where `Product ID` = 21

Update PROD.`prod+env+inventory+dataset`
Set `Product ID` = 11 where `Product ID` = 22

/*Checking Product id*/

Select distinct `Product ID` from PROD.`prod+env+inventory+dataset`

/*Importing Products data file*/
/*Checking Products data*/

Select * from  PROD.`products+(1)`;

/*Performing Left join between Inventory table and Product table

note:- the name of the columns should be same as in POWER BI dax measure 
other wise you have to built your report from scratch,
give alias name of the column as in Power bi */

Create table New_table as 
Select 
a.`Order Date (DD/MM/YYYY)` as `Order_Date_DD_MM_YYYY`,
a.`Product ID` as `Product_ID`,
a.`Availability` as `Availability`,
a.`Demand` as `Demand`,
b.`Product Name` as `Product_Name`,
b.`Unit Price ($)` as `Unit_Price`  from PROD.`prod+env+inventory+dataset` as a LEFT JOIN PROD.`products+(1)` as b 
on a.`Product ID`=b.`Product ID`

/*Checking New_table*/
Select * from prod.`New_table`