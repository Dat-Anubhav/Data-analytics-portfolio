'''Q4:- Create a new list containing the squares of the first 10 positive integers 
using a list comprehension. Print the new list.'''


# List comprehension syntax: [expression for item in iterable if condition]
l=[i**2 for i in range(1,11)]

# Displaying results
print(f"\nThe new list containing the squares of the first 10 positive integers = {l}\n")