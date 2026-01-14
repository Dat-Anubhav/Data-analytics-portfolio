
--UNION and UNION ALL--

--Creating new table
create table append1 (C1 int,C2 nvarchar(255),C3 int)
insert into append1 values (1,'A',7),
(2,'B',8),
(3,'C',9)



create table append2 (C1 int,C2 nvarchar(255),C3 int)
insert into append1 values (11,'AA',17),
(2,'B',8),
(33,'C1',91)

--UNION
Select C1,C2,C3 from append1
union -- remove duplicates
Select C1,C2,C3 from append2

--UNION ALL
Select C1,C2,C3 From append1
union all --just join two tabels by keeping duplicates
Select C1,C2,C3 FROM append2

--Numbers of columns present in the select list have to be same
--Data Types of the columns have to be same
--Order in which columns are written has to be the same

--Experiment: If datatypes are same
Select C1,C3,C2 from append1 
Union
Select C1,C2,C3 from append2 --C1 is int, C2 is nvarchar, C3 is int
--AS we can see it throws an error unable to convert nvarchar value 'A' to data type int.

--Experiment: If no of columns are not same
Select C1,C2 from append1
union
Select C1,C2,C3 from append2
--As we can see this also throws an error "All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists."


---Aliase names which are specified in 1st select statement will be assigned to the columns
Select C1 as [Column1],C2 as [Column2],C3 as [Column3] from append1
Union
Select C1 as [Col1],C2 as [Col2],C3 as [Col3] from append2
