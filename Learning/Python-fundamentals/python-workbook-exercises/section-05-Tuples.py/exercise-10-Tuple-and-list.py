'''Q10:- Create a tuple with the first 5 positive integers. Convert it to a list, 
append the number 6, and convert it back to a tuple. Print the resulting tuple.'''

# Creating a tuple with the first 5 positive integers 
tup=tuple(range(1,6))

# Displaying the tuple 
print("\nTuple with the first 5 positive integers = ",tup)

# Converting tuple tup into a list
lis=list(tup)

# Adding number 6 to the list
lis.append(6)

# Displaying the resulting tuple
print(f"\nAfter adding number 6, the tuple is = {tuple(lis)}\n")