
--LEFT and RIGHT ANTI JOIN--

Select * from table1 
select * from table2

--RIGHT Anti join
Select * from table1 right join table2 on table1.C1=table2.C1
where table1.C1 is null

Select * from table1 right join table2 on table1.C1=table2.C1
where table1.C1 is not null

--LEFT Anti join
Select * from table1 left join table2 on table1.C1 = table2.C1
where table2.C1 is null

Select * from table1 left join table2 on table1.C1=table2.C1
where table2.C1 is not null