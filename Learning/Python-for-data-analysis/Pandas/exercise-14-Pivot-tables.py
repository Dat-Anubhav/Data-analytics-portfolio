'''Q14:- Create a Pandas DataFrame with columns 'Date', 'Category', and 'Value'. 
Create a pivot table to compute the sum of 'Value' for each 'Category' by 'Date'.'''

import numpy as np
import pandas as pd

# Creating a date range for the 'Date' column
date_range=pd.date_range(start='2025-11-17', end='2025-12-31', freq='D')

# Creating a Pandas DataFrame with columns 'Date', 'Category', and 'Value'.
df=pd.DataFrame({'Date':np.random.choice(date_range, size = 20), 'Category':np.random.choice(['A','B','C'], size=20), 'Value':np.random.randint(1,100, size=20)})

# Displaying the dataframe
print("\nThe dateframe :- ")
print(df)

# Creating a pivot table to compute the sum of 'Value' for each 'Category' by 'Date'
pivot_table=df.pivot_table(values='Value', index='Date', columns='Category', aggfunc=sum)

'''Pivot tables in Pandas help organize and summarize data. With aggfunc='sum', 
they add up values for each group. If only one value is present, it shows that value; for more, 
it displays the total. NaN means there's no data for that group.'''

# Displaying the pivot table
print("\nPivot table :- ")
print(pivot_table)