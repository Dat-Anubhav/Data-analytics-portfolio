''' Q5:- s = {}
What is the type of 's'?'''

"""
Summary :- In this program we will find the type of s, where s is defined as s={}
"""

# an empty set is created using set() function and not {} because {} is used to create an empty dictionary
s={}
print(type(s))
# hence the type of s will be dictionary
# if we want to create an empty set then we will use set() function
s=set()
print(type(s))
# hence the type of s will be set