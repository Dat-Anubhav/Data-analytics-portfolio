'''Q1:- Create a dictionary with the first 10 positive integers as keys and their squares as values. 
Print the dictionary.'''

# Creating a dictionary with the first 10 positive integers as keys and their squares as values.
dict={i : i**2 for i in range(1,11)}

# Displaying results
print("\nA dictionary of positive integers as keys and their squares as values :- \n")

print(dict,"\n")