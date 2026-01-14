'''Q1:- Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. 
Replace all the elements in the third column with 1.'''

import numpy as np

arr1=np.random.randint(1,21, size=(5,5))

print("\nArray of shape(5,5) :- ",arr1,"\n")

# Replacing all the elements in the third column with 1.
# :means all the rows and ,2 is index number (0,1,2) i.e third column
arr1[:,2]=1

# Displaying result
print(arr1,"\n")