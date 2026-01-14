'''Q16:- Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. 
Apply a function that doubles the values of the DataFrame.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with 3 columns and 5 rows filled with random integers. 
df=pd.DataFrame(np.random.randint(1,10, size=(5,3)), columns=['A','B','C'])

# Displaying the original dataframe
print("\nThe dataframe :-")
print(df)

# Here both apply map and map produces same output
double_value=df.map(lambda x:x*2)

'''The key difference between applymap and map in Python (specifically with Pandas) is that 
applymap operates on every element of a DataFrame, while map operates on every element of a Series (single column).'''

'''In Pandas version (≥2.1.0), 
DataFrame.map and applymap are functionally the same due to the renaming/deprecation update'''

# Displaying the modified dataframe
print("\nModified dataframe :-")
print(double_value)