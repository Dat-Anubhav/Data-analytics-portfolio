'''Q6:- Create a set with duplicate elements and remove the duplicates using set methods. 
Print the modified set.'''

# The question asks to create a set with duplicate elements, 
# which is not possible because a set does not allow duplicates; 
# therefore, creating a tuple is the only way to achieve this.

st=(22,3,3,2,2,4,55,6,7,7,7,4.5)
print(f"\nWith duplicate elements = {st}\n")
# Converting tuple st into a set to remove duplicates
s=set(st)

# Displaying results
print(f"Without duplicate elements = {s} {type(s)}\n")