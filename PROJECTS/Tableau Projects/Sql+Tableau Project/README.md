Student Depression & Mental Health Analysis

Project Overview

This project explores the various factors contributing to depression among students. By analyzing variables such as academic pressure, financial stress, sleep duration, and family history, the goal is to identify high-risk patterns and provide insights for educational institutions to better support student well-being.

Tech Stack

    •	Database: MS SQL Server (Data Cleaning & Preparation)

    •	Visualization: Tableau Public

    •	Data Source: Student Mental Health Survey (CSV)

Key Analysis & SQL Features
  
    •	Age Grouping: Created custom age brackets in SQL to segment the student population.
  
    •	Categorical Mapping: Standardized "Male/Female" to "M/F" and converted boolean indicators (1/0) into readable "Yes/No" formats for better reporting.

    •	Identity Column: Added unique index identifiers to the dataset for precise row-level tracking in Tableau.

Interactive Dashboard Link:-

https://public.tableau.com/views/StudentDepressionAnalysis_17696264871320/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Key Findings

    •	The Sleep Factor: Students reporting less than 5 hours of sleep were significantly more likely to experience suicidal thoughts and depression.
  
    •	Academic Pressure: A direct correlation was observed between high academic pressure (scaled 1-5) and decreased study satisfaction.
  
    •	Family History: Students with a family history of mental illness showed a notable increase in depression risk, highlighting the need for early intervention programs.

    •	Dietary Impact: "Unhealthy" dietary habits were frequently associated with higher financial stress and lower academic performance.

Repository Contents
  
    •	SQLQuery-on Student Database.sql: Complete SQL script containing the data transformation and cleaning logic.

    •	Depression+Student+Dataset.csv: The raw data analyzed in the project.

    •	Project Screenshots.pdf: Visual guide of the dashboard pages and key metrics.
  
    •	Dashboard Link.docx: Direct access link to the Tableau Public workbook.

How to Use
  
  1.	Run the SQL script on your local server to see the cleaning process.
  2.	Open the Tableau link to filter data by Gender, Sleep Duration, or Financial Stress to see real-time updates on depression counts.

