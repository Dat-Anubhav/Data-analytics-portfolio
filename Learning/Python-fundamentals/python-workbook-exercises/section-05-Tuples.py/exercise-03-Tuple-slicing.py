'''Q3:- Print the first three elements, the last three elements, 
and the elements from index 2 to 5 of the tuple created in Assignment 1.'''

t=tuple(range(1,11))

# Displaying exercise 1 tuple
print(f"\nFirst 10 positive integers are:- {t}\n")
# Displaying first three elements
print(f"The first three elements are = {t[:3]}")
# Displaying last three elements
print(f"The last three elements are = {t[7:10]}")
# Displaying elements from index 2 to 5 
print(f"The elements from index 2 to 5 are = {t[2:5]}\n")

