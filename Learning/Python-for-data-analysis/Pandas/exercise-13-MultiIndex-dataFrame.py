'''Q13:- Create a Pandas DataFrame with a MultiIndex (hierarchical index). 
Perform some basic indexing and slicing operations on the MultiIndex DataFrame.'''

import numpy as np
import pandas as pd

arrays=[['A','A','B','B'],['one','two','one','two']]

ind=pd.MultiIndex.from_arrays(arrays, names=('Category','Sub-category'))

df=pd.DataFrame(np.random.randint(1,20, size=(4,3)),index=ind, columns=['Value 1','Value 2','Value 3'])

# Displaying dataframe to the user
print("\nThe dataframe :-")
print(df)

# Performing basic indexing operations on the MultiIndex DataFrame.
print("\nIndexing over category A :- ")
print(df.loc['A'])

# Performing basic slicing operations on the MultiIndex DataFrame.
print("\nSlicing at category B and sub-category 'two':-")
print(df.loc['B','two'])