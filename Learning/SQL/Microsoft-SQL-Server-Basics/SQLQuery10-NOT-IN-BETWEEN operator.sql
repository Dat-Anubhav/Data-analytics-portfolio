
--NOT,BETWEEN and IN operator

-- NOT operator
Select * from Employees
where not Firstname='Anubhav'

--NOT operator with IN operator
Select * from Employees
WHERE NOT Firstname IN ('Anubhav','Rishu')

--BETWEEN operator
Select * from EmployeeRecords
WHERE Salary between 75000 and 150000

--BETWEEN and AND operator 
Select * from EmployeeRecords
WHERE Salary  between  75000 and 150000

--Same thing can also be wriiten as 
Select * from EmployeeRecords
Where Salary>=75000 and Salary<=150000

Select * From EmployeeRecords

--IN operator
Select * from EmployeeRecords
Where Department IN ('IT','Marketing')