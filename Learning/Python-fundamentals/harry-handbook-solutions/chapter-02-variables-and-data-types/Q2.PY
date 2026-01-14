'''Q2:- Write a python program to find remainder when a number is divided by z'''

# Taking input from the user and converting it to integer using int()
a = int(input("enter the number that has to be diveded :- "))
b =  int(input("enter the number by which we have to divede:- "))

# Finding remainder using modulus operator %
c=a%b

# Printing the remainder
print("the remainder of a/b is ",c)