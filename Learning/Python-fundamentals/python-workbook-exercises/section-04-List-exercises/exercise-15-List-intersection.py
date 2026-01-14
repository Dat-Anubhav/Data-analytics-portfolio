'''Q15:- Write a function that takes two lists and returns a new list containing only 
the elements that are present in both lists. Print the intersected list.'''

# Defining a function to find intersection of two lists
def list_intersection(list1, list2):
    
    # Using a list comprehension to include only elements found in both lists
    return [i for i in list1 if i in list2]

# Creating the two list 
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Finding the intersection of the two lists using the function
intersection = list_intersection(list1, list2)

# Displaying results
print(f"\nList 1: {list1}")
print(f"\nList 2: {list2}")
print(f"\nIntersection: {intersection}\n")