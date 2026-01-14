'''Q5:-Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. 
Introduce some NaN values. Drop the rows with any NaN values.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with 4 columns and 6 rows filled with random integers.
df=pd.DataFrame(np.random.randint(1,20, size=(5,3)), columns = ['A','B','C'])

# Displaying the original dataframe to the user
print("\nOriginal dataframe :-")
print(df)

# Introducing some NaN values.
df.iloc[1,2]=np.nan
df.iloc[0,1]=np.nan
df.iloc[0,0]=np.nan

'''The iloc in pandas is used for selecting rows and columns from a 
DataFrame using integer-based (position-based) indexing, not by names or labels.'''

# Displaying dataframe with NaN values
print("\nDataframe with NaN values :- ")
print(df)

# Dropping NaN values from the dataframe
df.dropna(inplace=True)

# Displaying the dataframe with dropped NaN values
print("\nDataframe with dropped NaN values :- \n",df,"\n")
