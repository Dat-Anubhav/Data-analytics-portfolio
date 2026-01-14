'''Q11:- Create two NumPy arrays of shape (2, 3) and (3, 2). 
Perform matrix multiplication on these arrays.'''

import numpy as np
# Creating matrix 1
array1=np.random.randint(1,20, size=(2,3))

# Displaying matrix 1
print(f"\nMtrix 1 :- \n\n{array1}")

# Creating matrix 2
array2 = np.random.randint(1,20, size=(3,2))

# Displaying matrix 2
print(f"\nMatrix 2 :- \n\n{array2}")

# Performing matrix multiplication
mat_mul = np.dot(array1,array2)

# Displaying result
print(f"\nResult = \n\n{mat_mul}\n")