'''Q2:- Create a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'. 
Fill the DataFrame with random integers and access the element at row 'Y' and column 'B'.'''

import numpy as np

import pandas as pd

# Creating a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'.
df=pd.DataFrame(np.random.randint(1,20, size = (3,3)), columns = ['A','B','C'], index =['X','Y','Z'])

# Dislaying the original datframe
print("\nOriginal dataframe :- \n")
print(df)

# accessing the element at row 'Y' and column 'B'.
k=df.at['Y','B']

print("\nThe element at row 'Y' and column 'B' = ",k,"\n")