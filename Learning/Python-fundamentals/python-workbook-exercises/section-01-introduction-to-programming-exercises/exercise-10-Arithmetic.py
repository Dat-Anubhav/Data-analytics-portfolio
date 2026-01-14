'''Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b'''

"""
Summary:- This program reads two integers from the user and computes their sum, difference, and product.
"""

# taking input from user
a=int(input("enter the first integer :- "))
b=int(input("enter the second integer :- "))

# sum
sum=a+b

# difference
difference=a-b

# product
product=a*b

# quotient
quotient=a/b
# remainder
remainder = a%b

#log10a
# to find log10a we have to import math module which is already in built module in python

import math
log=math.log10(a) 

# power
power=a**b# in python it is represented by ** no eed to import any module

#final output 
print(f"two integers a and b are {a} and {b}\n\
Sum of a and b is = {sum}\n\
Difference of a and b is = {difference}\n\
Product of a and b is = {product}\
\nQuotient of a nd b is {quotient}\
\nRemainder of a nd b is = {remainder}\
\nlog of a to the base 10 i.e log10a is = {log}\
\n {a} to the power {b} is = {power}")

# greeting meassage
print("THANKS FOR USING OUR SERVICES")