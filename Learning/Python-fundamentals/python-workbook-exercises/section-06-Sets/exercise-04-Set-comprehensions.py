'''Q4:- Create a new set containing the squares of the first 10 positive integers using a set comprehension. 
Print the new set.'''

# Creating a new set containing the squares of the first 10 positive integers using a set comprehension.
s=set(i**2 for i in range(1,11))

# Displaying the set
print(f"\nThe set containing the squares of the first 10 positive integers = {s}\n")