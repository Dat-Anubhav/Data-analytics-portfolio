
--RIGHTJOIN--

Use Our_employee_details

Select * from table1
Select * from table2

Select * from table1 right join table2 on table1.C1=table2.C1

--Only want C1,C2,C3 columns to be displayed, performing right join with the alias name of the tables
Select a.C1,a.C2,b.C3 from table1 a right join table2 b on a.C1=b.C1

/*In the join condition, NULL never equals NULL, so rows with NULL in the join column do not match. 
In a RIGHT (or LEFT) JOIN those unmatched rows appear with NULLs for the columns from the other table.*/


