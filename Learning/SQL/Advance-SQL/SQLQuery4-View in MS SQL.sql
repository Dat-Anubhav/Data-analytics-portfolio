
--VIEWS in MS SQL server--

--A View is a virtual table,it is a stored SQL Query
--It helps in reducing the complexity of the code
--It helps in implementing security,such as u can show certain employeeid employee details such as 4,5,6

Select * into emp_bkp from [dbo].[EmployeeRecords]

Select * from emp_bkp

--Creating a view of only the FirstName of the employees
Create view view1 as(
Select FirstName from emp_bkp)

Select * from view1

--Updating the view
Update view1
Set FirstName = 'Anubhav' where FirstName = 'Rishu'

--NOTE:- If we make changes such as update or delete in the view ,it will also effect the main table too 

--Checking the View table
Select * from view1

--Creating view2 which consist every detail except the salary

Create view view2 as (
Select EmployeeID,FirstName,LastName,Department from emp_bkp) 

--Checking View2
Select * from view2