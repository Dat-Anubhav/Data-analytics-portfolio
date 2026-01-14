'''Q9:- Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. 
Print the original and transposed matrices.'''

def transpose_matrix(matrix):
    # Creating the transposed matrix using nested list comprehensions.
    # The outer loop iterates over each column index.
    # The inner loop collects the elements from each row at the given column index.
    transpose=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[1]))]

    return transpose

# Forming a 3x3 matrix (as a nested list)
matrix=[
[1,2,3],
[4,5,6],
[7,8,9]
]

# Displaying the original matrix and the transposed version of the matrix
transposed=transpose_matrix(matrix)
# Displaying the original matrix 
print("\nA 3*3 matrix :-")
for row in matrix:
    
    print(row)
# Displaying the transpose matrix
print("\nIts transpose will be :-")
for row in transposed:
    
    print(row)