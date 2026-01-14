'''Q12:- Create a Pandas DataFrame with a datetime index ranging from '2021-01-01' to '2021-12-31' 
and one column filled with random integers. Compute the rolling mean with a window of 7 days.'''

import numpy as np
import pandas as pd

data_range=pd.date_range(start='2021-01-01', end='2021-12-31', freq='D')

df=pd.DataFrame(data_range, columns=['date'])
df['Value'] = np.random.randint(1,100, size = len(data_range))
df.set_index('date', inplace=True)

# Displaying the dataframe
print("\nThe Dataframe :- ")
print(df)

# Computing the rolling mean with a window of 7 days.
rolling_mean = df.rolling(window=7).mean()
# Calculates the rolling mean (moving average) over a 7-day window, which smooths out daily 
# fluctuations and helps reveal trends in the data by averaging each value with the previous 6 days.

# Displaying result
print("\nRolling mean of 7 days :-")
print(rolling_mean)