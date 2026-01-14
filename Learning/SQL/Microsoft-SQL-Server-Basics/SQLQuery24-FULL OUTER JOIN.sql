
--FULL OUTER JOIN--

Select * from table1
select * from table2

Select * from table1 full outer join table2 on table1.C1=table2.C1

--only Selected columns 
Select a.C1,a.C2,b.C3 from table1 a full outer join table2 b on a.C1=b.C1

-- FULL OUTER JOIN returns all rows from both tables.
-- It includes matched rows, plus unmatched rows from each side with NULLs for the missing table’s columns.
--(inner join + left join + right join )

