'''Q4 :- What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''

"""
Summary :- In this program we will find the length of the given set 
by adding the same values but of different data types.
"""

s=set()# created an empty set

s.add(20)#integer value
s.add(20.0)#float value
s.add('20')# string value

# all the three values are different because they are of different data types
# hence all the three values will be added to the set

print(len(s))
# hence the length of the set will be 3