'''Q5:- Create two NumPy arrays of shape (3, 4) filled with random integers. 
Perform element-wise addition, subtraction, multiplication, and division.'''

import numpy as np

arr1 = np.random.randint(1,20, size=(3,4))

arr2 = np.random.randint(1,20, size=(3,4))

# Displaying array 1 to the user  
print(f"Array 1:- \n{arr1}")

# Displaying array 2 to the user
print(f"\nArray 2 :- \n{arr2}")

# Performing addition
add=arr1+arr2
print(f"\nAddition of array 1 and array 2 = \n{add}")

# Performing subtraction
sub=arr1-arr2
print(f"\nSubtraction of array 1 and array 2 = \n{sub}")

# Performing multiplication
mul=arr1*arr2
print(f"\nMultiplication of array 1 and array 2 = \n{mul}")

# Performing division
div=arr1/arr2
print(f"\nDivision of array 1 and array 2 = \n{div}\n")