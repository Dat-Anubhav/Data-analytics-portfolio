'''Q15:- Create a NumPy array of shape (4, 4) filled with random integers. 
Use boolean indexing to set all elements greater than 10 to 10.'''

import numpy as np

# Creating a NumPy array of shape (4, 4) filled with random integers. 
array = np.random.randint(1, 21, size=(4, 4))

# Displaying the original array to the user
print("Original array :- \n")
print(array)

# Using boolean indexing to set all elements greater than 10 to 10
array[array > 10] = 10

# Displaying the modified array
print("\nModified array :- \n\n")
print(array,"\n")