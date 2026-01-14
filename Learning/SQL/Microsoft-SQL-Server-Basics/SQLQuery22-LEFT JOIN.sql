
--LEFT JOIN or LEFT OUTER JOIN--

Select * from table1
Select * from table2

Select * from table1 left join table2 on table1.C1=table2.C1

--Left outer join
select * from table1 left join table2 on table1.C1=table2.C1

--As we can see both left join and left outer join gives the same output

--Performing left join by alias name
Select a.C1,a.C2,b.C3 from table1 a left join table2 b on a.C1=b.C1

/*Use LEFT JOIN when you want all rows from the left table,
and matching rows from the right table if they exist.
Example: list every customer and show their orders if any; customers without orders still appear with NULL in order columns.*/
