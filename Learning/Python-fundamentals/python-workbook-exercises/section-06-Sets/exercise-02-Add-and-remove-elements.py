'''Q2:- Add the number 11 to the set created in Assignment 1. 
Then remove the number 1 from the set. Print the modified set.'''

# Creating a set with the first 10 positive integers.
s={i for i in range(1,11)}

print(f"\nA set with the first 10 positive integers = {s} type:- {type(s)}")

# Adding number 11 to the set s
s.add(11)

# Displaying the modified set 
print(f"\nAdding number 11 to the set = {s}")

# Removing the number 1 from the modified set s
s.remove(1)

# Displaying the final set
print(f"\nFinal set after removing number 1 from the modified set = {s}\n")