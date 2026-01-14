'''Q12:- Create a dictionary with the first 5 positive integers as keys and their squares as values.
 Create a new dictionary with keys and values swapped. Print the new dictionary.'''

# Creating a dictionary with the first 5 positive integers as keys and their squares as values.
dictionary={i:i**2 for i in range(1,6)}

# Creating a new dictionary with keys and values swapped.
new_dictionary={v:k for k,v in dictionary.items()}

# Displaying results
print(f"\nA dictionary with the first 5 positive integers as keys and their squares as values.")
print(f"{dictionary}   {type(dictionary)}")

print(f"\nA new dictionary with keys and values swapped.")
print(f"{new_dictionary}   {type(new_dictionary)}\n")

