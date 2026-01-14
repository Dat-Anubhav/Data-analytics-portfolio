'''Q18:- Create a Pandas Series with 5 random text strings. Convert all the strings to uppercase.'''

import pandas as pd

# Creating a Pandas Series with 5 random text strings.
ds=pd.Series(['apple','banana','cherry','orange'])

# Displaying the original series
print("\nOriginal series:-")
print(ds)

# Converting all the strings to uppercase.
upper_ds=ds.str.upper()

# Displaying result
print("\nModified dataseries :- ")
print(upper_ds)