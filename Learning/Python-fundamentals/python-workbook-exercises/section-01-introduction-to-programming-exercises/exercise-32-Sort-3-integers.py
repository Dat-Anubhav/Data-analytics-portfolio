'''Q32:-Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value'''


i1=int(input("\nEnter the first integer :- "))
i2=int(input("\nEnter the second integer :- "))
i3=int(input("\nEnter the third integer :- "))

# Calculating the largest number among the three integers
mx=max(i1,i2,i3)

# Calculating the smallest number among the three intgers
mn=min(i1,i2,i3)

# Calculating the Second place number
sn=(i1+i2+i3)-mn-mx

# Displaying results
print(f"Among {i1}{i2}{i3} numbers \n Largest one is = {mx}\n Smallest one is = {mn}\n\
 Ascending order of the numbers are = {mn},{sn},{mx}")
