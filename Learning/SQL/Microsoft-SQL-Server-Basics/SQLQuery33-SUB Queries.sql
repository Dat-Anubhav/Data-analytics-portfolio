
--SUB QUERIES--

--Creating a new table to practice sub queries

--Creating table of Customers
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100)
);

--Creating a table of Orders
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);



-- Inserting data into Customers table
INSERT INTO Customers (customer_id, customer_name, email)
VALUES 
(1, 'Alice Smith', 'alice@example.com'),
(2, 'Bob Johnson', 'bob@example.com'),
(3, 'Charlie Brown', 'charlie@example.com');

-- Inserting data into Orders table
INSERT INTO Orders (order_id, customer_id, order_date, amount)
VALUES 
(101, 1, '2024-07-15', 250.00),
(102, 1, '2024-08-05', 300.00),
(103, 2, '2024-08-10', 150.00),
(104, 3, '2024-06-25', 100.00);

--Checking status of both the table

--Customers table
Select * from Customers

--Orders table
Select * from Orders

--Finding customers who order in the month of August
Select * from Customers
where customer_id in(
Select Distinct customer_id from Orders where order_date Between '2024-08-01' and '2024-08-31'
)

--Finding customers who did not order in the month of August
Select * from Customers
where customer_id in (
Select distinct customer_id from Orders where order_date not between '2024-08-01' and '2024-08-31')

--Finding employees from the employees records whose salary is more than the average salary
Select * from EmployeeRecords

Select * from EmployeeRecords
where Salary >(Select avg(Salary) from EmployeeRecords)

--Finding the average salary to check whether the output is correct or not
Select avg(Salary) as [Average salary] from EmployeeRecords

--test
Select * from EmployeeRecords
where Salary >avg(Salary)
--This will throw an error because:- An aggregate may not appear in the WHERE clause unless it is in a subquery contained in a HAVING clause
--or a select list, and the column being aggregated is an outer reference.
