
--SELF JOIN--

Select * from table1

Select * from table1 self join table1 on table1.C1=table1.C1

--Creating new table to practice self join

--Creating table
Create table student(StudentID int,name varchar(max),BestfriendID int);

Insert into student(StudentID,name,BestfriendID)
Values(1,'Jethalal',2),
(2,'Tarak',1),
(3,'jai',4),
(4,'veeru',3),
(5,'akshay',null);

Select * from student

Select * from student a left join student b on a.StudentID=b.BestfriendID 

--Displaying Selected columns only: student name and bestfriend name
Select a.name as [student name],b.name as [Bestfriend] from student a join student b on a.StudentID=b.BestfriendID  

