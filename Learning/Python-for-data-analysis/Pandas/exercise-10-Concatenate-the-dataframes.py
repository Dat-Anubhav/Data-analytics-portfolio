'''Q10:- Create two Pandas DataFrames with different columns. 
Concatenate the DataFrames along the rows and along the columns.'''

import numpy as np
import pandas as pd

# Creating two Pandas DataFrames with different columns.
df1=pd.DataFrame({'key1':['A','B','C','D'],'value1':np.random.randint(1,20, size = 4)})
df2=pd.DataFrame({'key2':['e','f','g','h'],'value2':np.random.randint(1,20, size = 4)})

# Displaying dataframes to the user
print("\nDataframe 1 :-\n")
print(df1)
print("\nDataframe 2 :=\n")
print(df2)

# Concatenating the DataFrames along the rows
df=pd.concat([df1,df2], axis=0)

# Displaying result
print("\nConcatenated dataframe along the rows :-\n")
print(df)

# Concatenating the DataFrames along the column
df=pd.concat([df1,df2], axis=1)

# Displaying result
print("\nConcatenated dataframe along the column :-\n")
print(df)