'''Q17:- Create a Pandas DataFrame with 3 columns and 6 rows filled with random integers. 
Apply a lambda function to create a new column that is the sum of the existing columns.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with 3 columns and 6 rows filled with random integers.
df=pd.DataFrame(np.random.randint(1,10, size=(6,3)), columns=['A','B','C'])

# Displaying the original dataframe
print("\nOriginal dataframe :-")
print(df)

# Applying a lambda function to create a new column that is the sum of the existing columns.
df['Total']=df.apply(lambda x:x.sum(), axis=1)

''' # Use map for element-wise operations on a Series (single column).
# Use applymap (now DataFrame.map in Pandas ≥2.1) for element-wise operations across all cells in a DataFrame.
# Use apply for applying functions across rows or columns (axis-wise) in a DataFrame, suited for more complex 
 or aggregation tasks.'''

# Displaying result
print("\nNew dataframe :-")
print(df)



