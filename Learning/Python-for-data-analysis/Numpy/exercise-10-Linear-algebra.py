'''Q10:- Create a NumPy array of shape (3, 3) representing a matrix. 
Compute its determinant, inverse, and eigenvalues.'''

import numpy as np

# Creating a NumPy array of shape (3, 3) representing a matrix.
matrix = np.random.randint(1,20, size=(3,3))

# Displaying the matrix to the user
print("\nThe matrix :- ")
print(matrix)

# Computing its determinant, inverse, and eigenvalues.
determinant = np.linalg.det(matrix)

inverse = np.linalg.inv(matrix)

eigenvalues = np.linalg.eigvals(matrix)

# Displaying results
print(f"\nDeterminant = {round(determinant,3)}\
\n\nInverse = \n{inverse}\
\n\neigenvalues = {eigenvalues}\n")