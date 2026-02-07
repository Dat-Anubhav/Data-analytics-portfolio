Google Play Store Data Cleaning and Pre-processing

This project demonstrates a comprehensive data cleaning and transformation pipeline applied to a real-world Google Play Store marketplace dataset. The objective was to convert a complex, inconsistent dataset into a structured, high-integrity format optimized for Exploratory Data Analysis (EDA) and predictive modeling.

Project Overview:-

The raw dataset contained over 9,600 records with significant inconsistencies, including mixed data types (strings and numeric values), special characters in financial fields, and inconsistent file size units. This project follows a systematic approach to data sanitization, feature engineering, and schema optimization.

Key Technical Steps:-

    1.) Data Sanitization: Cleaned the Installs and Price columns by removing special characters such as +, , and $, converting them into numerical formats suitable for analysis.
    
    2.) Feature Engineering:
        
        – Decomposed the Last Updated field into Date, Month, and Year features.

        – Standardized the Size column by converting all values (KB and MB) into a uniform numerical scale.

        – Derived a quantitative Minimum Age feature from categorical content ratings.

    3.) Missing Value Management: Identified and handled missing values across 16 columns, resulting in a complete dataset containing 9,659 records.

    4.) Data Type Optimization: Converted object-type columns into appropriate integer, float, and datetime formats to enable statistical operations and improve computational efficiency.

    5.) Integrity Checks: Removed redundant entries and validated the final dataset to ensure zero missing values and a consistent schema.

Technical Stack

    • Language: Python

    • Libraries: Pandas, NumPy, Matplotlib, Seaborn

    • Environment: Jupyter Notebook

    • Data Source: Google Play Store dataset (Krish Naik Data Science curriculum)

Deliverables

    • Cleaned Dataset: Google-playstore-cleaned-data.csv containing 9,659 non-null records across 16 optimized columns.

    • Processing Pipeline: google-playstore-data-cleaning.ipynb documenting the complete data cleaning and preprocessing workflow.

Project Roadmap

The output of this project (`Google-playstore-cleaned-data.csv`) serves as the primary data source for the next phase: **Exploratory Data Analysis**. 

In the subsequent repository, I utilize this high-integrity data to perform deep-dive visualizations and extract market-driven business insights.


Project Structure
    
    • google-playstore-data-cleaning.ipynb – Primary notebook containing the data transformation and preprocessing logic.

    • Google-playstore-cleaned-data.csv – Final dataset ready for exploratory analysis, reporting, or machine learning models.

Project Purpose:-

This project highlights hands-on expertise in data cleaning, feature engineering, and preparing complex real-world datasets for professional analytical and machine learning workflows.

