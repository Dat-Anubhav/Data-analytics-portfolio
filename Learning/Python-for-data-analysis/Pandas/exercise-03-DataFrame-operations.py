'''Q3:- Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. 
Add a new column that is the product of the first two columns.'''

import numpy as np
import pandas as pd

# Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers.
df=pd.DataFrame(np.random.randint(1,20, size = (5,3)), columns =['A','B','C'])

# Displaying original data frame to the user
print("\nData frame :- ")
print(df)

# Adding a new column that is the product of the first two columns i.e D=A*B.
df['D']=df['A']*df['B']

# Displaying modified data frame to the user 
print("\nAdding a new column that is the product of the first two columns.")
print(df)
