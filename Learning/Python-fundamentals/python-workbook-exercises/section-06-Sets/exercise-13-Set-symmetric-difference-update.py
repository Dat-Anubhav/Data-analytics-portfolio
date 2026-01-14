'''Q13:- Create two sets and update the first set with the symmetric difference of the two sets. 
Print the modified first set.'''
# Creating set 1
s1={i for i in range(1,11)}

# Creating set 2
s2={j for j in range(1,11) if(j%2==0)}

# Displaying both the set to the user for reference
print("\nSet 1 = ",s1)
print("Set 2 = ",s2)

# Finding symmetric difference of s1 and s2
sy=s1.symmetric_difference(s2)

# Displaying symmetric difference of s1 and s2
print(f"Symmetric difference of s1 and s2 = {sy}")

# updating the first set with the symmetric difference of the two sets.
s1.symmetric_difference_update(s2)

# Displaying updated s1
print("\nUpdated s1 = ",s1)
print()