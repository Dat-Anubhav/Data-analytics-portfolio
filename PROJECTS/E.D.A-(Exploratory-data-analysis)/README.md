Google Play Store Exploratory Data Analysis (EDA)

This project performs an in-depth exploratory analysis of the Google Play Store marketplace to uncover the underlying factors that drive app popularity and user engagement. By analyzing a cleaned dataset of over 9,600 applications, this study provides data-driven insights into market trends, category performance, and pricing strategies.

Project Overview:-

The objective was to transition from data engineering to business intelligence. This analysis focuses on identifying market leaders, understanding rating distributions, and exploring the correlation between technical specifications (like app size) and market success (installs and ratings).

Key Analytical Insights:-

      •	Market Composition: Identified "Family," "Game," and "Tools" as the most saturated categories, indicating high competition but also high consumer demand.
      
      •	Quality Benchmarking: Discovered that 271 applications maintain a perfect 5.0-star rating. Notably, the "CS & IT Interview Questions" app leads the Family category in this elite group.
      
      •	Installation Patterns: Conducted a granular analysis of install volumes across genres to distinguish between "niche" high-rated apps and "mass-market" high-install apps.

      •	Monetization & Engagement: Evaluated the Free vs. Paid ratio and its impact on user sentiment, providing a clear picture of how pricing affects an app's rating trajectory.

      •	Demographic Targeting: Analyzed the distribution of content ratings and "Min Age" requirements to understand how developers target different age groups.

Prerequisites & Data Origin:-

This analysis is performed on the high-integrity dataset generated during the **Google Play Store Data Cleaning** phase. 

The preceding cleaning project was essential to standardize mixed data types, normalize units (KB/MB), and handle missing values, ensuring the statistical accuracy of the visualizations presented here.

Technical Stack
      
      •	Language: Python
  
      •	Libraries: Pandas, NumPy, Matplotlib, Seaborn

      •	Environment: Jupyter Notebook

      •	Data Source: Cleaned Google Play Store dataset (processed in the previous [Data Cleaning Project])

Deliverables
      
      •	Analysis Pipeline: E.D.A -on-google-playstore-cleaned-data.ipynb containing the full visualization suite including distribution plots, heatmaps, and categorical breakdowns.

      •	Validated Data: Google-playstore-cleaned-data.csv, the 9,659-record dataset used as the "single source of truth" for this analysis.

Project Structure

      •	E.D.A -on-google-playstore-cleaned-data.ipynb: The primary analytical notebook featuring statistical summaries and visualization-driven storytelling.

      •	Google-playstore-cleaned-data.csv: The high-integrity dataset generated from the preceding data cleaning phase.

Project Purpose: 

This repository demonstrates an advanced ability to translate raw data into actionable business intelligence. It highlights proficiency in data storytelling, statistical visualization, and the ability to extract meaningful trends from a complex marketplace ecosystem.

