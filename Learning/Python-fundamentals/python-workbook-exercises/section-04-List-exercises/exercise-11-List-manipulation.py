'''Q11:- Create a list of the first 10 positive integers. 
Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. 
Print the modified list.'''
# Creating a list of the first 10 positive integers.
lis=[i for i in range(1,11)]

# Displaying the list to the user for reference
print("\nOriginal list = ",lis)

# Removing the elements at indices 2, 4, and 6,
del lis[2]
del lis[4]
del lis[6]

# inserting an element '99' at index 5.
lis.insert(5,'99')

# Displaying the modified list to the user
print("Modified list = ",lis,"\n")