'''Q5:- Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. 
Print the new dictionary.'''

# Creating a new dictionary containing the cubes of the first 10 positive integers 
# using a dictionary comprehension. 
dict={i:i**3 for i in range(1,11)}

# Displaying results
print(f"\nThe dictionary of the first 10 positive integer cubes :- \n")

print(dict,"\n")