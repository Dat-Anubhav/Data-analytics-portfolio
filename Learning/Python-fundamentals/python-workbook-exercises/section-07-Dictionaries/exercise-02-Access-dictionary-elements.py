'''Q2:- Print the value of the key 5 and the keys of the dictionary created in Assignment 1.'''

# Creating a dictionary with the first 10 positive integers as keys and their squares as values.
dict={i:i**2 for i in range(1,11)}

# Displaying dictionary to the user for reference
print("\nThe dictionary is = ",dict)

# Displaying key 5 value to the user 
print(f"\nValue of key 5 = {dict.get(5)}")

# Displaying all the keys of the dictionary dict
print(f"\nThe keys of the dictionary are :- {list(dict.keys())}\n")
