'''Q5:- Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)'''

"""
Summary :- In this program we will count the number of zeroes in a tuple.
"""

# creating a tuple
a=(7,0,8,0,0,9)

# using count() function to count the number of zeroes in the tuple
c=a.count(0)

# displaying the result to the user
print(f"number of zeroes in the tuple {a} \n is :- {c}")