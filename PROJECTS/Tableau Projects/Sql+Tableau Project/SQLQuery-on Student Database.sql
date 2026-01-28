
--Creatingn ew database for SQL+Tableau Project

Create database depression

--importing flat file

--Checking imported data
Select * from [dbo].[Depression+Student+Dataset]

--Modifying Gender column
Select Gender, count(*) from [dbo].[Depression+Student+Dataset]
Group by Gender

--No.of males is > than no. females

--representing males by M and Females by F
Update [Depression+Student+Dataset]
set Gender='M' where Gender = 'Male'

Update [Depression+Student+Dataset]
set Gender='F' where Gender = 'Female'

--Checking data
Select * from [Depression+Student+Dataset]

--Checking for null values
Select * from [Depression+Student+Dataset] where Gender is null

Select * from [Depression+Student+Dataset] where Gender = ''

--Checking Age column
Select Age, count(*) [No.of people of this age] from [Depression+Student+Dataset]
group by Age
order by Age desc

--Creating a new Age Group column
Alter table [dbo].[Depression+Student+Dataset]
Add Age_Group varchar(max)

--checking created Age_Group column
Select * from [Depression+Student+Dataset]

--As we can see age group column has been created successfully, but it has only null values

--Filling null values with condition
Update [Depression+Student+Dataset]
set Age_Group = 
case when Age between 18 and 24 then 'A1'
Else case when age between 25 and 30 then 'A2'
else 'A3' end end

--Checking data
Select * from [dbo].[Depression+Student+Dataset]

--Counting no.of People in each age group
Select Age_Group, count(*) [No.of student] from [Depression+Student+Dataset]
group by Age_Group

--Getting Information schema for student depression table
Select * from INFORMATION_SCHEMA.COLUMNS where table_name like 'Depression+Student+Dataset'

Select Academic_Pressure,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Academic_Pressure

Select Study_Satisfaction,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Study_Satisfaction

Select Sleep_Duration,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Sleep_Duration


Select Dietary_Habits,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Dietary_Habits

Select Have_you_ever_had_suicidal_thoughts,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Have_you_ever_had_suicidal_thoughts

Select Study_Hours,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Study_Hours

Select Financial_Stress,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Financial_Stress


Select Family_History_of_Mental_Illness,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Family_History_of_Mental_Illness

Select Depression,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Depression

Select Age_Group,count(*) [Count] from [dbo].[Depression+Student+Dataset]
group by Age_Group

--Adding an Index column
Alter table [dbo].[Depression+Student+Dataset]
Add Index_Column int identity(1,1)

--Checking data
Select * from [Depression+Student+Dataset]

--Modifying the Depression column, Addig yes for 1 and no for 0
Update [Depression+Student+Dataset]
set Depression='Yes' where Depression=1

--It shows conversion failed because depression column is bit type 
--Converting depression column into varchar type

Alter table [dbo].[Depression+Student+Dataset]
Alter Column Depression varchar(max)

--Now runnning the Previous Update Query 
-- checking database for changes

Select * from [Depression+Student+Dataset]

--Updating no for 0
Update [Depression+Student+Dataset]
Set Depression='No' where Depression='0'

--Checking data
Select * from [Depression+Student+Dataset]

--counting no. of Student under depression and no.of student are not
Select Depression,count(*) [Count] from [dbo].[Depression+Student+Dataset] group by Depression
