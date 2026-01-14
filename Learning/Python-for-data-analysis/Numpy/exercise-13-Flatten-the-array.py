'''Q13:- Create a NumPy array of shape (5, 5) filled with random integers. 
Flatten the array and then reshape it back to (5, 5).'''

import numpy as np

# Creating a NumPy array of shape (5, 5) filled with random integers.
arr = np.random.randint(1,20, size = (5,5))

# Displaying the array to the user
print("\nOriginal array :- ")
print(arr)

# Flattening the array
flatten_array = arr.flatten()

# Displaying the Flatten array
print("\nFlatten array :-")
print(flatten_array)

# Reshaping the flatten array
k=flatten_array.reshape(5,5)

# Displaying the reshaped flatten array
print("\n Flatten array reshaped :- ")
print(k)