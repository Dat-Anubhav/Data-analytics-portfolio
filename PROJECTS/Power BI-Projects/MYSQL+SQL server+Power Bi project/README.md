Supply Chain Inventory & Demand Analysis (End-to-End BI)
Project Overview
This project demonstrates a full-cycle Business Intelligence solution, from database design and ETL to advanced data visualization. It focuses on analyzing inventory availability against market demand to identify supply shortages and profit opportunities.
Tech Stack
•	Database: MS SQL Server (Test Env), MySQL (Prod Env) 
•	Visualization: Power BI 
•	Language: SQL, DAX 
Project Workflow
1. Database Implementation & ETL
•	Test Environment: Created the test_env database in SQL Server and imported flat files for products and inventory.
•	Data Transformation: Applied LEFT JOIN operations to consolidate inventory and product datasets into a unified New_table for reporting.
•	Production Migration: Replicated the architecture in MySQL for the PROD environment, ensuring column aliases remained consistent with Power BI measures.
2. Data Cleaning
•	Identified and corrected data entry errors (e.g., mapping Product ID 21 to 7 and ID 22 to 11) using SQL UPDATE statements to maintain data integrity.
3. Power BI Analytics & DAX
Developed a series of calculated measures to drive business insights:
•	Total Supply Shortage: [Total Demand] - [Total Availability].
•	Total Loss: Calculated based on shortages and unit prices to quantify missed revenue.
•	Profitability: Created conditional logic to determine profit/loss status for each product line.
Key Files
•	SQLQuery-Joining...sql: SQL Server scripts for the initial development phase.
•	MySQL script-PROD ENV...sql: Scripts for the production environment and migration logic.
•	Power Bi Report.pbix: The final dashboard.
•	Technical_Implementation_Documentation.pdf: Detailed step-by-step technical guide.
How to Run
1.	Execute the SQL scripts in your local SQL Server or MySQL instance to set up the databases.
2.	Open the .pbix file in Power BI Desktop.
3.	Update the data source settings to point to your SQL/MySQL instance.

