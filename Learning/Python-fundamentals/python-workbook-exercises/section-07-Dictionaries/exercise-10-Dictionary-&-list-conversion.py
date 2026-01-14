'''Q10:- Create a dictionary with the first 5 positive integers as keys and their squares as values. 
Convert the dictionary to a list of tuples and print it.'''

# Creating a dictionary with the first 5 positive integers as keys and their squares as values.
d={i:i**2 for i in range(1,6)}

# Displaying the dictionary to the user for reference
print("\nA dictionary with the first 5 positive integers as keys and their squares as values:- ")
print(d,"\n")

# "Converting all the dictionary items into a tuple
print("\nConverting all the dictionary items into a tuple:-")
t=tuple(d.items())

# Diplaying the tuple to the user for reference
print(t,"\n")

# Converting the tuple into a list
print("\nConverting the tuple into a list")
lis=list(t)

# Displaying the list to the user
print(lis,"\n")