'''Q10:- Write a function that takes a nested list and flattens it into a single list. 
Print the original and flattened lists.'''

# Forming a function that takes a nested list and flattens it into a single list.
def nested_list_function(nested_list):
    lis=[] # creating an empty list to store the elements of the nested list.
    for i in nested_list:# Loop over each sublist in the nested list

        for j in i:# Loop over each element in the current sublist
        
            lis.append(j)# Adding the element to the flattened list

    return lis
# Creating a nested list
nested_list=[[1,2,3],[4,5,6],[7,8,9]]

# Displaying results
print("\nThe nested list is = ",nested_list)

print(f"\nFlattened list = {nested_list_function(nested_list)}\n")