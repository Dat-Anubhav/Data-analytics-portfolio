'''Q4:- Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers. 
Compute the row-wise and column-wise sum.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with 3 columns and 4 rows filled with random integers. 
df=pd.DataFrame(np.random.randint(1,20, size = (4,3)), columns = ['A','B','C'])

# Displaying the original dataframe to the user
print("\nOriginal dataframe :- ")
print(df)

# Computing the row-wise and column-wise sum.
row_sum=df.sum(axis=1)
column_sum=df.sum(axis=0)

# Displaying results
print(f"\nRow wise sum :- \n{row_sum}")
print(f"\nColumn wise sum :- \n{column_sum}\n")