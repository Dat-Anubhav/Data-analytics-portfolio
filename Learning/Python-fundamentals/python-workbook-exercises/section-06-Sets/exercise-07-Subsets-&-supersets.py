'''Q7:- Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. 
Check if the second set is a subset of the first set and if the first set is a superset of the second set. 
Print the results.'''
# Creating first 5 positive integer set
s1={i for i in range(1,6)}

# Displaying the set to the user for reference
print("\nThe set s1 = ",s1)

# Creating first 3 positive integer set
s2={i for i in range(1,4)}

# Displaying the set to the user for reference
print("\nThe set s2 = ",s2)

# Verifying the superset condition.
if(s1.issuperset(s2)):

    print(f"\nSet s1 is a superset of set s2\n")

else:

    print(f"\ns1 and s2 are two different sets\n")