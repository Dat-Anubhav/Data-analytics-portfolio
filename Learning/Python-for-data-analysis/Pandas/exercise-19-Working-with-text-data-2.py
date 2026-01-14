'''Q19:- Create a Pandas Series with 5 random text strings. Extract the first three characters of each string.'''

import pandas as pd

# Creating a Pandas Series with 5 random text strings.
ds=pd.Series(['apple','banana','cherry','orange'])

# Displaying the original series
print("\nOriginal series :- ")
print(ds)

# Extracting the first three characters of each string.
extract_string=ds.str[:3]

# Displaying result
print("\nFirst three characters of each string :-")
print(extract_string)