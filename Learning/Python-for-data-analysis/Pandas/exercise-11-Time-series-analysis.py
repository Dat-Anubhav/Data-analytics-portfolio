'''Q11:- Create a Pandas DataFrame with a datetime index and one column filled with random integers. 
Resample the DataFrame to compute the monthly mean of the values.'''

import numpy as np
import pandas as pd

date_time=pd.date_range(start='2025-01-01', end='2025-12-31', freq='D')

df=pd.DataFrame(date_time, columns=['date'])

# Intoducing data column filled with random integers
df['Data'] = np.random.randint(1,100, size=len(date_time))

# Setting date as index
df.set_index('date', inplace=True)

# Displaying the dataframe
print("\nDataframe :-")
print(df)

# Resampling the DataFrame to compute the monthly mean of the values.
mm=df.resample('M').mean()
# The resample function is used in pandas to change the frequency of time series data, 
# enabling you to group and aggregate the data into different time intervals like monthly, weekly, yearly, etc.

# Displaying the datframe with monthly mean
print("\nMonthly mean :-")
print("\n",mm,"\n")