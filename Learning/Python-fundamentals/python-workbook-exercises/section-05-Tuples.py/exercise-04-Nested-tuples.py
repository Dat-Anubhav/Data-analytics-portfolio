'''Q4:- Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.'''

mat=(
(1,2,3),
(4,5,6),
(7,8,9))

print("3*3 matrix is :- ")

for i in mat:
# printing the 3*3 matrix mat
    print(i)

# Displaying element of third row and second column
print(f"\nElement of third row and second column = {mat[1][2]}")
