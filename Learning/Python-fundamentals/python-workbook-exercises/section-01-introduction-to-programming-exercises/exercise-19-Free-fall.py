'''Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s2. You can use the formula vf = vi2 + 2ad to compute the
final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known'''

"""
Summary :- This program determines how quickly an object when dropped from a certain height hits the ground.
"""

# importing math module to use math.sqrt() function
import math

# Asking user to enter the height from which the object is dropped
d=float(input("\nEnter the height from which the object is dropped in meters:- "))

#Acceleration due to gravity = 9.8m/s^2 Given in question
a=9.8

# Initial velocity = 0 m/s^2 Given in question
vi= 0

#Calculating the final velocity of the object when it hits the ground 
vf=math.sqrt(vi**2+2*a*d)

# Displaying the result i.e final velocity of an object when it hits the ground
print(f"\nIf the object is dropped from the hieght of {d} meters , \n\
then it will reach up to the velocity of {round(vf,1)}m/s at the time of hitting the ground")

print("\nSTAY SAFE WHILE EXPERIMENTING :)\n")