
--INNER JOIN--

Create Table table1(C1 int,C2 nvarchar(max))

insert into table1(C1,C2)
Values
(1,'A'),
(1,'B'),
(2,'C'),
(null,'D'),
(3,'E'),
(7,'DA');

Create table table2(C1 int, C3 nvarchar(max))

insert into table2(C1,C3)
values 
(1,'XA'),
(2,'MB'),
(2,'NX'),
(NULL,'MO'),
(4,'XY'),
(5,'TF');

Select * from table1
Select * from table2

--Inner join on table1 C1 and table2 C1
Select * from table1 inner join table2 on table1.C1=table2.C1

--Just want C1,C2 and C3 column
Select table1.C1,table1.C2,table2.C3 from table1 inner join table2 on table1.C1=table2.C1

--Giving alias name to table1 and table2
Select a.C1,a.C2,b.C3 from table1 a inner join table2 b on a.C1=b.C1

--If we write just join, then also it will work in the same way
Select A.C1,A.C2,B.C3 from table1 A join table2 B on A.C1=B.C1

/*INNER JOIN is used to combine two tables, but it keeps only the rows that match in both tables.
For example, if we join Customers and Orders on CustomerID,
we only see customers who actually have orders (customers without orders are not shorwn, and orders without a valid customer are also not shown).
Another example: joining Employees and Departments on DepartmentID will show only employees who are assigned to an existing department.
*/