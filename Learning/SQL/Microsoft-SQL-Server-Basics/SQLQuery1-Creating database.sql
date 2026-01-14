
-- Creating Database

Create database Our_employee_details

use Our_employee_details

-- Table 1 
CREATE TABLE Employees
(EmployeeID INT PRIMARY KEY,
Firstname VARCHAR(30),
Lastname VARCHAR(30),
Department VARCHAR(30),
Salary DECIMAL(10,2),
HiredDate   DATE);


INSERT INTO Employees (EmployeeID, Firstname, Lastname, Department, Salary, HiredDate)
VALUES
(1, 'Anubhav','Srivastav','Data Science','100000', '2022-01-15' ),
(2, 'Rishu', 'Srivastav','Web Development', '120000', '2023-03-23'),
(3, 'Minato', 'Namikaze','Finance', '150000', '2024-07-10'),
(4, 'Ben', 'Tennyson', 'Marketing', '170000', '2025-09-30'),
(5, 'Harry', 'Potter', 'IT', '200000', '2026-02-20');


