'''Q4:- Create a NumPy array of shape (5, 5) with random integers. 
Extract the elements on the border.'''

import numpy as np

# Creating an NumPy array of shape (5, 5) with random integers.
arr=np.random.randint(1,20, size=(5,5))

# Displaying the original array to the user
print("\nOriginal array :-")
print(arr)

# Extracting the elements on the border
k=arr[:,4]
k=k.reshape(5,1) #reshaping it into a 5*1 matrix

# Displaying the extracted elements matrix
print("\nExtracted elements matrix is :- ")
print(k,"\n")