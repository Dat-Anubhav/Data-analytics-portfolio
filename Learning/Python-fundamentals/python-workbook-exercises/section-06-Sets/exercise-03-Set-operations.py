'''Q3:- Create two sets: one with the first 5 positive integers and another with the first 5 even integers. 
Perform and print the results of union, intersection, difference, and symmetric difference operations 
on these sets.'''
# Creating set s1 with the first 5 positive integers
s1={i for i in range(1,11)}

# Displaying set s1 to the user for reference
print("\nSet s1 =",s1)

# Creating set s2 with the first 5 even integers
s2=set(range(2,11,2))

# Displaying set s2 to the user for reference
print("\nSet s2 =",s2)

# UNION
su=s1.union(s2) # either use | or .union

# INTERSECTION
si=s1 & (s2) # either use & or .intersection

# DIFFERENCE
sd=s1.difference(s2) # either use - or .difference

# SYMMETRIC DIFFERENCE
sy=s1.symmetric_difference(s2) # either use ^ or .symmetric_difference

# Displaying results
print(f"\nUnion of s1 & s2 = {su}\
\n\nIntersection of s1 & s2 = {si}\
\n\nDifference of s1 & s2 = {sd}\
\n\nSymmetric difference of s1 and s2 = {sy}\n")

