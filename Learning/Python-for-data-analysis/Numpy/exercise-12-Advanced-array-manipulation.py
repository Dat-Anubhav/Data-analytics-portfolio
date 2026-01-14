'''Q12:- Create a NumPy array of shape (3, 3) with values from 1 to 9. 
Reshape the array to shape (1, 9) and then to shape (9, 1).'''

import numpy as np

# Creating a NumPy array of shape (3, 3) with values from 1 to 9.
arr=np.random.randint(1,9, size=(3,3))

# Displaying the original array
print(f"\nOriginal array :- \n\n{arr}")

# Reshaping the original array
arr2=arr.reshape(1,9)

# Displaying the reshaped array
print(f"\nReshaped array :- \n\n{arr2}")

# Reshaping the reshaped array
arr3=arr2.reshape(9,1)

# Displaying the final array
print(f"\nFinal array :- \n\n{arr3}\n")