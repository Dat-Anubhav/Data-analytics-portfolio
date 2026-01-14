'''Q6:- Create two dictionaries: one with keys as the first 5 positive integers 
and values as their squares, and another with keys as the next 5 positive integers 
and values as their squares. Merge these dictionaries into a single dictionary and print it.'''

# Creating a dictionary for the squares of the first 5 positive integers
d1={i:i**2 for i in range(1,6)}

# Displaying dictionary d1 to the user for reference
print("\nA dictionary of the squares of the first 5 positive integers.",d1)

# Creating a dictionary for the squares of the next 5 positive integers (6 to 10)
d2={j:j**2 for j in range(6,11)}

# Displaying dictionary d2 to the user for reference
print("\nDictionary of the squares of the next 5 positive integers:",d2)

# Merging the two dictionaries into d1
d1.update(d2)

# Displaying merged dictionary d1
print("\nMerged dictionary = ",d1,"\n")