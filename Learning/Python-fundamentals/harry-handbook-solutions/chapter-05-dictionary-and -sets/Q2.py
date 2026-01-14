'''Q2:-Write a program to input eight numbers from the user and display all the unique numbers (once)'''

"""
Summary :- In this program we will input eight numbers from the user and display all the unique numbers (once) 
for that we will use set data structure because set only stores unique values.
"""

# set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
l1=int(input("eneter the number :- "))
l2=int(input("eneter the number :- "))
l3=int(input("eneter the number :- "))
l4=int(input("eneter the number :- "))
l5=int(input("eneter the number :- "))# here is the input of all the 8 numbers from the user
l6=int(input("eneter the number :- "))
l7=int(input("eneter the number :- "))
l8=int(input("eneter the number :- "))

#in python  an empty set is created using set() function and not {}
#because {} is used to create an empty dictionary

s=set()#made an empty set in which i will store all the other inputs from the user

# a set can input only one value at a time so we will use add() function to add the values 
# adding more than one value at a time will give an error

s.add(l1)
s.add(l2)
s.add(l3)
s.add(l4)
s.add(l5)
s.add(l6)
s.add(l7)
s.add(l8)

# added all the 8 numbers to the set
print("all the unique numbers are :- ",s)