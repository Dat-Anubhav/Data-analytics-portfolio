'''Q13:- Create a default dictionary where each key has a default value of an empty list. 
Add some elements to the lists and print the dictionary.'''

# Import the defaultdict class from the collections module
from collections import defaultdict

# Creating a default dictionary with empty lists as default values
def_dic=defaultdict(list)

# Add values to the lists for each key 
def_dic['a'].append(1) # Add 1 to the list for key 'a'
def_dic['b'].append(2) # Add 2 to the list for key 'b'
def_dic['c'].append(3) # Add 3 to the list for key 'c'

# Display the contents of the default dictionary
print("\n",def_dic,"\n")

'''This code creates a special kind of dictionary that gives you an empty list every time you use a 
new key, so you don't get errors.
If you add something for a key like 'a', it starts with an empty list and then adds your value. 
You can keep adding more numbers to these lists using .append().'''