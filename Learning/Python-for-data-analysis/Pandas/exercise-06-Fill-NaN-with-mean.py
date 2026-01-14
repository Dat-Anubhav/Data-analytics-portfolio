'''Q6:- Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. 
Introduce some NaN values. Fill the NaN values with the mean of the respective columns.'''

import numpy as np
import pandas as pd

# Creating a Pandas DataFrame with 3 columns and 5 rows filled with random integers. 
df=pd.DataFrame(np.random.randint(1,20, size=(5,3)), columns = ['A','B','C'])

# Displaying original dataframe
print("\nOriginal datframe :-")
print(df)

# Introducing some NaN values.
df.iloc[3,2]=np.nan
df.iloc[4,1]=np.nan
df.iloc[0,0]=np.nan

# Displaying Dataframe with NaN values
print("\nDataframe with NaN values :- \n")
print(df)

#  Filling the NaN values with the mean of the respective columns.
df.fillna(df.mean(),inplace=True)

# Displaying result
print("\nDataframe filled with NaN values with the mean of the respective columns :- \n")
print(df)

'''Mean imputation is a simple method where missing data values are replaced with the 
average value of the available data for that variable. It helps keep the dataset complete, 
making it easier to analyze and model, especially when only a small amount of data is missing. 
However, it reduces data variability and can weaken relationships between variables, potentially 
skewing results if used improperly in complex analyses. Despite these limitations, 
it offers a quick and practical solution in many real-world scenarios when data is missing at random.'''