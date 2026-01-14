'''Q14:- Create a NumPy array of shape (5, 5) filled with random integers. 
Use fancy indexing to extract the elements at the corners of the array.'''

import numpy as np

# Creating a NumPy array of shape (5, 5) filled with random integers.
arr=np.random.randint(1,20, size = (5,5))

# Displaying the original array
print("\nOriginal array :- \n")
print(arr)

# Extracting the corner elements through fancy indexing
corner=arr[[0,0,-1,-1],[0,-1,0,-1]]
# Imagine the two lists like sets of row and column positions. 
# Each item from the first list lines up with an item from the second list, 
# forming a pair—just like (row, column) coordinates. 
# NumPy uses each of these pairs to pick out the exact elements you want from your array

# Displaying the corner elements
print("\nCorner elements are :- \n")
print(corner)