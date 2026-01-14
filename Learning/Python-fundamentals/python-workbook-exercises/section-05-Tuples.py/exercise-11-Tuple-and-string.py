'''Q11:- Create a tuple with the characters of a string. 
Join the tuple elements into a single string. Print the string.'''

# Tuple with the characters of a string
tup=('Hi',"i","am","Anubhav","Srivastav")

# Displaying the tuple to the user for reference
print(f"\nthe tuple is = {tup}")

'''The syntax for the .join() method in Python:- separator.join(iterable)

separator: The string you want to insert between each element.
iterable: A sequence (like a list, tuple, or set) containing only string elements.'''

join=' '.join(tup) # The .join() method works only if all the elements are string

# Displaying results
print("\nThe string is = ",join)
