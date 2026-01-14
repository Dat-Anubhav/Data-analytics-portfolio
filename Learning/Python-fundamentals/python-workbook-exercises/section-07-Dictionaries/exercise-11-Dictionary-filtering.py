'''Q11:- Create a dictionary with the first 10 positive integers as keys and their squares as values. 
Create a new dictionary containing only the key-value pairs where the key is even. 
Print the new dictionary.'''

# Creating a dictionary with the first 10 positive integers as keys and their squares as values.
dictionary={i:i**2 for i in range(1,11)}

# Creating a new dictionary containing only the key-value pairs where the key is even.
new_dictionary={k: v for k,v in dictionary.items() if(k%2==0)}

# Displaying both the dictionaries
print(f"\nA dictionary with the first 10 positive integers as keys and their squares as values.")
print(dictionary)

print("\nA new dictionary containing only the key-value pairs where the key is even.")
print(new_dictionary,"\n")