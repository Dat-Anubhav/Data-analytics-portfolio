'''Q1:- Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers.
Set the index to be the first column.'''

import pandas as pd

import numpy as np

# Creating a Pandas DataFrame with 4 columns and 6 rows filled with random integers.
df=pd.DataFrame((np.random.randint(1,20, size = (6,4))), columns = ['A','B','C','D'])

# Displaying original dataframe
print("\nOriginal dataframe :- ")
print("\n\n",df,"\n")

print("\nSetting index to column A :-")

# Setting the index to be the first column. 
df.set_index('A', inplace=True)

# Displaying result
print("\n",df)