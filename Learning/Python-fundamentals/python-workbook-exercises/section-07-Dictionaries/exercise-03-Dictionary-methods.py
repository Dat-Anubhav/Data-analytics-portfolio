'''Q3:- Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. 
Print the modified dictionary.'''
# Recreating the dictionary of exercise 1
dict={i:i**2 for i in range(1,11)}

# Displaying the dictionary to the user for reference
print("\nThe dictionary is = ",dict)

# Adding a new key-value pair(11,121)
dict[11]=121

# Displaying the modified dictionary
print("\nAdding a new key-value pair(11,121):- ",dict)

# Removing the key 1 pair
dict.pop(1)

# Displaying the modified dictionary
print(f"\nRemoving the key 1 pair:- {dict}\n")