'''Q14:- Write a function that rotates a list by n positions. Print the original and rotated lists.'''

# Creating a function that rotates a list by n positions.
def rotate_list(lis,n):
    
    # The slice lis[n:] takes all elements from n to the end,
    # lis[:n] takes elements from start to n (not including n).
    # Concatenating them completes the rotation.
    return lis[n:] + lis[:n]

# Creating the list
original_list = [1,2,3,4,5,6,7,8,9]

# # Calling the function to rotate the list by 2 positions
rotated_list = rotate_list(original_list,2)

# Displaying results
print("\nThe original list = ",original_list)
print("\nThe rotated list = ",rotated_list,"\n")