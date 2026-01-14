'''Q14:- Create a tuple with duplicate elements. 
Convert it to a set to remove duplicates and print the resulting set.'''

# Creating tuple with duplicate elements
tup=(11,22,33,45,"hello",'a','a','b','b','b')

# Displaying tuple to the user for reference
print(f"\nTuple with duplicate elements = {tup}")

# Converting the tuple tup into a set to remove duplicates 
s=set(tup)

# Displaying tuple without duplicate elements
print(f"\nTuple without duplicate elements = {s}\n")

