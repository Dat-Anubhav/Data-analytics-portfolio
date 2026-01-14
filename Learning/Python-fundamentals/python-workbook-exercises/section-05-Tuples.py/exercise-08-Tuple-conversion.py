'''Q8:- Convert a list of the first 5 positive integers to a tuple. Print the tuple.'''

# Creating a list of first 5 positive integers
ls=[i for i in range(1,6)]

print(f"\nList of first 5 positive integers = {ls} {type(ls)}")
# Converting list into a tuple
tup=tuple(ls)

# Displaying results 
print(f"\nTuple of first 5 positive integers = {tup} {type(tup)}\n")