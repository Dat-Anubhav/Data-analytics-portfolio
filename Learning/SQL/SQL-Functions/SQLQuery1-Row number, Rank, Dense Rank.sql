
--Row number,Rank & Dense Rank--

Create Database SQL_Functions 

--Creating table

CREATE TABLE Students (
    student_name VARCHAR(100),
    subject VARCHAR(100),
    marks INT
);


INSERT INTO Students (student_name, subject, marks)
VALUES 
-- Marks for Alice
('Alice', 'Math', 85),
('Alice', 'Science', 88),
('Alice', 'English', 92),

-- Marks for Bob
('Bob', 'Math', 90),
('Bob', 'Science', 78),
('Bob', 'English', 85),

-- Marks for Charlie
('Charlie', 'Math', 85),
('Charlie', 'Science', 82),
('Charlie', 'English', 80),

-- Marks for David
('David', 'Math', 92),
('David', 'Science', 91),
('David', 'English', 89),

-- Marks for Eve
('Eve', 'Math', 90),
('Eve', 'Science', 85),
('Eve', 'English', 87),

-- Marks for Frank
('Frank', 'Math', 75),
('Frank', 'Science', 72),
('Frank', 'English', 78),

-- Marks for Grace
('Grace', 'Math', 85),
('Grace', 'Science', 89),
('Grace', 'English', 90);

--View Table
Select * from Students

--Row number function
Select *, Row_number() over(order by marks) as [Row number]
from Students

--Note:- In case of a tie row numbers are assigned randomly

--Rank function
Select *, Rank() over(order by marks desc) as [Rank]
from Students

--Note:- In rank function, if there's a tie next rank/ranks will be skipped

--Dense Rank function
Select *, Dense_rank() over (order by marks desc) as [Rank]
from Students

--Note:- In dense rank function,if there's a tie ranks will not be skipped

    --Using Partition

--Row number function
Select *, Row_number() Over(Partition by subject order by marks) as [Row number]
from Students

    --Partition by  student name
Select *, ROW_NUMBER() over(partition by student_name order by marks) as [Row number]
from Students

--Rank function
Select *, Rank() over(Partition by subject order by marks) as [Rank]
from Students
    
    --Partition by student name
Select *, rank() over(partition by student_name order by marks) as [Rank]
from Students

--Dense rank function
Select *, Dense_rank() over(partition by subject order by marks) as [Rank]
from Students

    --Partition by student name
Select *, Dense_rank() over(partition by student_name order by marks) as [Rank]
from Students