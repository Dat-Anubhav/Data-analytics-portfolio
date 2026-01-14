'''Q7:- Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:

sum =(n)(n + 1)/2'''

"""
Summary:- This program reads a positive integer from the user and calculates
the sum of all integers from 1 to that integer using the formula sum = n(n + 1)/2.
""" 

n=int(input("enter the postive integer :- "))

# formula for sum of first n positive integers
sum=n*(n+1)/2
 
print(f"the sum of first positive integers from 1 to {n} is :- {sum}")
