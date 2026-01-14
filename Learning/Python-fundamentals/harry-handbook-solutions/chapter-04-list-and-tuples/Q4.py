'''Q4 :- Write a program to sum a list with 4 numbers.'''

"""
Summary :- In this program we will sum a list with 4 numbers.
"""
# creating a list with 4 numbers

list1=[34,56,78.9,22.5]

sum1=list1[0]+list1[1]+list1[2]+list1[3]# this is one way to sum the list

print(f"sum of the list {list1} is \n sum:- {sum1}")

#                   OR

#Using sum() function to sum the list elements.

l = [22,5,78,12,55]

print(f"SUM of the list2 i.e {l}\n")

print(sum(l))

# if you have named a variable as sum then sum function will not work
# because python gets confused between the variuable sum and function sum() 
# sum() function is an inbuilt function in python to sum the list elements
