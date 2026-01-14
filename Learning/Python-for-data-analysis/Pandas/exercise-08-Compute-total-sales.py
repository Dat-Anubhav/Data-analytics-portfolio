'''Q8:- Create a Pandas DataFrame with 3 columns: 'Product', 'Category', and 'Sales'. 
Fill the DataFrame with random data. Group the DataFrame by 'Category' and compute the total sales for each category.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with 3 columns: 'Product', 'Category', and 'Sales'.
df=pd.DataFrame({'Product' : np.random.choice(['product 1','product 2','product 3'], size = 10),'Category':np.random.choice(['A','B','C'], size = 10),'Sales':np.random.randint(1,20, size = 10)})

# Displaying the dataframe to the user
print("\nDataframe :- \n")
print(df)

# Grouping the DataFrame by 'Category' and computing the total sales for each category.
grouped = df.groupby('Category')['Sales'].sum()

# Displaying result
print("\nTotal sales by category :- ")
print("\n",grouped,"\n")