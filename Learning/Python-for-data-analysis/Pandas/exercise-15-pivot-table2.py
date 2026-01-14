'''Q15:- Create a Pandas DataFrame with columns 'Year', 'Quarter', and 'Revenue'. 
Create a pivot table to compute the mean 'Revenue' for each 'Quarter' by 'Year'.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with columns 'Year', 'Quarter', and 'Revenue'. 
df=pd.DataFrame({'Year':np.random.choice([2020,2021,2022], size=12),'Quarter':np.random.choice(['Q1','Q2','Q3','Q4'], size=12), 'Revenue':np.random.randint(1,100, size=12)})

# Displsying the dataframe 
print("\nThe dataframe :- ")
print(df)

# Creating a pivot table to compute the mean 'Revenue' for each 'Quarter' by 'Year'.
pivot_table=df.pivot_table(values='Revenue', index='Year',  columns='Quarter', aggfunc='mean')

# Displaying the pivpot table
print("\nThe dataframe :-")
print(pivot_table)