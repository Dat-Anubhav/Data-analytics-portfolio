'''Q9:- Create two Pandas DataFrames with a common column. 
Merge the DataFrames using the common column.'''

import numpy as np
import pandas as pd

# Creating two Pandas DataFrames with a common column. 
df1=pd.DataFrame({'key':['a','b','c','d'], 'value1': np.random.randint(1,20, size = 4)})
df2=pd.DataFrame({'key' : ['a','b','c','e'], 'value2':np.random.randint(1,20, size = 4)})

# Displaying dataframes to the user
print("\nDataframe 1 :-\n")
print(df1)
print("\nDataframe 2 :-\n")
print(df2)

# Merging the DataFrames using the common column.
df=pd.merge(df1,df2, on='key')

# Displaying the merged dataframe
print("\nMerged dataframe :-\n")
print(df)