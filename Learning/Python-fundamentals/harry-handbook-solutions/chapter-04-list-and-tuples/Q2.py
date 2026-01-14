'''Q2:- Write a program to accept marks of 6 students and display them in a sorted
manner.'''

"""
Summary :- In this program we will take the input from the user to enter the marks of 6 students
and then display them in a ascending order.
"""

# taking the user input to enter the marks of 6 students
s1=int(input("enter the marks of the first student :-"))
s2=int(input("enter the marks of the second student :-"))
s3=int(input("enter the marks of the third student :-"))
s4=int(input("enter the marks of the fourth student :-"))
s5=int(input("enter the marks of the fifth student :-"))
s6=int(input("enter the marks of the sixth student :-"))

# Option 1 taking int input from the user

stlist=[s1,s2,s3,s4,s5,s6]
print("student list is :- ",stlist)
m=sorted(stlist)
print("the sorted list is :- ",m)

# Option 2 without taking int input from the user

#Using key=int to sort the list numerically instead of ASCII code.

# stlist = ['12', '23', '123', '45', '67', '78']
# m = sorted(stlist, key=int) # Convert to int for sorting
# print("the numerically sorted list is :- ", m)

"""Note:- if you dont take the input in int then it will sorted 
according to ASCII code hence 123 can come before 45 use input 
in int or specify it in sorted method as sorted(stlist, key=int)

what is ASCII code:- 

Ascii code is a unique number assigned to each character and symbol
so that computers can store, process and transmits the data in a series of numbers.
for example ascii code of '1' is 49 and ascii code of '4' is 52."""
# Therefore in ASCII code 123 comes before 45 because 1 comes before 4 in ascii code