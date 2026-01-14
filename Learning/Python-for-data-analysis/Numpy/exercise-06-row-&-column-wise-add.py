'''Q6:- Create a NumPy array of shape (4, 4) with values from 1 to 16. 
Compute the row-wise and column-wise sum.'''

import numpy as np

# Creating a NumPy array of shape (4, 4) with values from 1 to 16.
arr=np.arange(1,17).reshape(4,4)

# Displaying the original array to the user
print("\nOriginalarray :-\n")
print(arr)

# Computing the row-wise addition
for i in arr:
    s=0
    # Adding the elements of first row and so on
    for j in i:

        s=s+j
    
    # Displaying the sum
    print(f"\nSum of row {i} = {s}")

# Displaying the original array to the user for reference
print(f"\nOriginal array :-\n\n{arr}")

# Computing the column-wise sum.
m=0
while(m<4):
    s=0
    for l in arr[:,m]: # Adding the column elements

        s=s+l
    # Displaying the sum
    print(f"\nSum of column {m+1} = {s}\n")
    m+=1