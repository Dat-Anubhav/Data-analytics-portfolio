''' Q18:-The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place'''

"""
Summary :- Calculating the volume of cylinder to 1 decimal places
"""
#  importing math function to use exact value of pi
import math

# taking user input for radius r and height h of the cylinder
r=float(input("\nEnter the radius of the cylinder :- "))
h=float(input("\nEnter the height of the cylinder :- "))

# As we know volume of cylinder = pi*r*r*h
volume= math.pi*r**2*h

# round() funtion is an inbuilt function which rounds of the value to the nearest integer 
# for example :- 3.2 output :- 3
#                4.7 output :- 5
# note:- python 3's round(), 0.5 one's rounds to nearest even integer 
# for example :- 2.5 output :- 2
#                3.5 output :- 4                                

# Displaying the volume of a cylinder upto 1 decimal places.
print("\nVolume of cylinder = ", round(volume,1))
