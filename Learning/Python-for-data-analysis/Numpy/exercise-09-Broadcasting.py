'''Q9:- Create a NumPy array of shape (3, 3) filled with random integers. 
Add a 1D array of shape (3,) to each row of the 2D array using broadcasting.'''

import numpy as np

array=np.random.randint(1,20, size=(3,3))

row_array=np.random.randint(1,20, size=(3,) )

# Displaying the original and 1D array to the user
print("\nOriginal array :-")
print(array)

print("\n1D array :- ")
print(row_array)

# Adding the 1D array to each row of the 2D array using broadcasting
res=array+row_array

# Displaying result
print("\nresulting array :-  ")
print(res)