'''Q1:- Create a tuple with the first 10 positive integers. Print the tuple.'''

# tuple() function is used to construct tuples from other iterable objects or to create an empty tuple if called without arguments.
# You can use loops to access/print tuple elements, just not to modify them 
# we can not make changes in the original tuple, it is fixed. 

t=tuple(range(1,11))

# Displaying results
print(f"\nFirst 10 positive integers are:- {t}")

