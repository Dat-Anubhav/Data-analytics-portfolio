'''Q15:- Use the filter function to filter out all odd numbers from a list of integers. 
Test with different lists.'''

# Creating a list
num = [1,2,3,4,5,6,7,8,9]

# Displaying the list to the user
print("\nOriginal list = ",num)

# Using the filter function with a lambda to remove all odd numbers from the list of integers
filter_lam = list(filter(lambda i:i%2!=0,num))

# Displaying the filtered list
print("\nFiltered list = ",filter_lam,"\n")