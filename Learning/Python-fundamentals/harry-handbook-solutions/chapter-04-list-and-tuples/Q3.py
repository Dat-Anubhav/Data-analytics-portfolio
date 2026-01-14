''' Q3 :- Check that a tuple type cannot be changed in python.'''

"""
Summary :- In this program we will create a tuple and then try to change its value.
we will see that tuple type cannot be changed in python.
"""

# creating a tuple
mytuple=(12,24,34.6,22.5)

# print(float(mytuple))# it will give an error because tuple type cannot be changed

# if we want to convert tuple into string or list type then it is possible
# comment the above line to see the result
 
print(str(mytuple))# it will work because tuple can be converted into string type

print(list(mytuple))# it will work because tuple can be converted into list type

# tuples are immutable i.e they cannot be changed
# they can only be converted to string or list type  

# hence type conversion of tuple is not possible only possible to convert it into string
# or list type