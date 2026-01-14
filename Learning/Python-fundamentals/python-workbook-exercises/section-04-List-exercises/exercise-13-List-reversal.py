'''Q13:- Write a function that takes a list and returns a new list with 
the elements in reverse order. Print the original and reversed lists.'''

# Creating a function that takes a list and returns a new list with the elements in reverse order.
def  reverse_order(lis):

    new_list = sorted(lis,reverse=True)

    return new_list

# Creating the list
lis=[1,2,3,4,5,6,7,8,9]

# Displaying results
print("\nOriginal list =",lis)

print("\nReversed list = ",reverse_order(lis),"\n")