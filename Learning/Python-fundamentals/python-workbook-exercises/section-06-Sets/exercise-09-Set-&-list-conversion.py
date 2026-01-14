'''Q9:- Create a set with the first 5 positive integers. 
Convert it to a list, append the number 6, and convert it back to a set. 
Print the resulting set.'''
# Creating a set with the first 5 positive integers. 
s={i for i in range(1,6)}

# Displaying set created above to the user for reference
print("\nThe set =",s)

# Converting set s into a list
lis=list(s)

# Adding number 6 to the list 
lis.append(6)

# Converting back to a set
ss=set(lis)

# Displaying results
print(f"\nAfter adding number 6 to the set = {ss}\n")