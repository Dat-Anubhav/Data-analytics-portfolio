
--ISNULL and COALESCE--
--Database -profit DB

--Creatig table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255)
);


INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber, Address)
VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@example.com', '555-1234', '123 Elm St'),
(2, 'Bob', 'Smith', NULL, '555-5678', NULL),
(3, 'Charlie', 'Williams', 'charlie.williams@example.com', NULL, '456 Oak St'),
(4, 'Diana', 'Brown', NULL, NULL, '789 Pine St'),
(5, 'Eve', 'Davis', 'eve.davis@example.com', '555-8765', NULL);

--VIEW TABLE
Select * from Customers

--ISnull
Select isnull(Email,'Not available') [Email], isnull(PhoneNumber, 'Not available') [PhoneNumber], isnull(Address,'Not available') [Address] from Customers

--COALESCE
Select coalesce(Email,PhoneNumber,Address,'Not available') as [Coalesce] from Customers

--Finding the contact info of customer Bob
Select coalesce(Email,PhoneNumber,Address,'Not available') as [Customer contact info] from Customers where FirstName like 'Bob'