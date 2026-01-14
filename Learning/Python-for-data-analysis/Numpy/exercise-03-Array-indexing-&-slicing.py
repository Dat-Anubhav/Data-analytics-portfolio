'''Q3:- Create a NumPy array of shape (6, 6) with values from 1 to 36. 
Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.'''

import numpy as np

# Creating a NumPy array of shape (6, 6) with values from 1 to 36.
arr=np.arange(1,37).reshape(6,6)

# Displaying the original array to the user
print("\nOriginal array:- ")
print(arr)

# Displaying the modified array
print("\n Modified array :- ")
print("\n",arr[2:6,1:4],"\n")