'''Q7:- Create a Pandas DataFrame with 2 columns: 'Category' and 'Value'. 
Fill the 'Category' column with random categories ('A', 'B', 'C') and 
the 'Value' column with random integers. Group the DataFrame by 'Category' 
and compute the sum and mean of 'Value' for each category.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with 2 columns: 'Category' and 'Value'.
df=pd.DataFrame({'Category': np.random.choice(['A','B','C'], size = 10), 'Value' : np.random.randint(1,20, size = 10)})

# Displaying the dataframe
print("\nDataframe :- \n")
print(df)
