'''Q14:- Use the map function to apply a lambda function that squares each number 
in a list of integers. Test with different lists.'''

# Creating a list
num=[1,2,3,4,5,6,7,8,9]

# Displaying the list to the user
print("\nOriginal list = ",num)

# Using the map function to apply a lambda function that squares each number in a list of integers.
map_lam = list(map(lambda i:i**2,num))

# Displaying the squared list
print("\nSquared list = ",map_lam,"\n")