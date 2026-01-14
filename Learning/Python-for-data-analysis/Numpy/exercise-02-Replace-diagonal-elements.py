'''Q2:- Create a NumPy array of shape (4, 4) with values from 1 to 16. 
Replace the diagonal elements with 0.'''

import numpy as np

# Creating a NumPy array of shape (4, 4) with values from 1 to 16.
arr=np.arange(1,17)
k=arr.reshape(4,4)

# Displaying the array to the user
print("\nOriginal array :- ")
print(k)

# Replacing the diagonal elements with 0.
np.fill_diagonal(k,0)

# Displaying results
print("\nModified array :- ")
print(k)