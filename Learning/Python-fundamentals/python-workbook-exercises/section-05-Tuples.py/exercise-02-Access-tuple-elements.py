'''Q2:- Print the first, middle, and last elements of the tuple created in Assignment 1.'''

t=tuple(range(1,11))

# Displaying assignment 1 tupple
print(f"\nFirst 10 positive integers are:- {t}\n")

# The varibales first and last will hold first and last element 
# and by using * we can assign rest of the middle elements to middle variable

first,*middle,last=t # unpacking tupple

# Displaying first element
print("\nFirst element = ",first)
# Displaying middle elements
print("\nMiddle elements = ",middle)
# Displaying last element
print("\nLast element = ",last)