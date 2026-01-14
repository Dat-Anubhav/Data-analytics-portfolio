'''Q12:- Create two lists of the same length. Use the `zip` function to 
combine these lists into a list of tuples and print the result.'''

list1=[1,2,3,4,5,6,7,8,9]

list2=['a','b','c','d','e']

# Displaying list 1 to the user for reference
print("\nList 1 = ",list1)

# Displaying list 2 to the user for reference
print("\nList 2 = ",list2)

# Using the zip function to combine these lists into a list of tuples
zip_list=list(zip(list1,list2))

# Displaying the zipped list to the user
print("\nZipped list = ",zip_list,"\n")