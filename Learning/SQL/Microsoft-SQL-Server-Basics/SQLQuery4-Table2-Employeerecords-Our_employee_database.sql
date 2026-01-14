use Our_employee_details

--Creating Table 2 in Our_employee_details Database--

CREATE TABLE EmployeeRecords
(EmployeeID NVARCHAR(50),
Firstname NVARCHAR(50),
Lastname NVARCHAR(50),
Department NVARCHAR(50),
Salary DECIMAL(10,2)
);

INSERT INTO EmployeeRecords (EmployeeID, FirstName, LastName, Department, Salary)
VALUES
(1, 'Anubhav', 'Srivastav', 'Data Science', 100000.22),
(2, 'Rishu ', 'Srivastav', 'Web development', 120000.34),
(3, 'Anubhav', 'Chitransh', 'Marketing', 150000.56),
(4, 'Minato', 'Namikaze', 'IT', 90000),
(5, 'Rishu', 'Srivastav', 'Finance', 175000.89),
(6, 'Yuji', 'Itadori', 'Marketing', 90000);

/*VARCHAR stores normal English text, 
while NVARCHAR stores text from any language (like Hindi/Chinese) and emojis, but uses more space./*