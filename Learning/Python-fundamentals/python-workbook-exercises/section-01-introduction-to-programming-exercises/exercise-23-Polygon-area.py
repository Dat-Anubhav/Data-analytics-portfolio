'''Q23:-A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:-
area =(n * s^2)/(4 * tan (π/n))
Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.'''

"""
Summary:-calculating area of a ploygon whose number of sides and their length is given.
"""

# importing math module to use tan function and pi constant.
import math

# Taking user input to get the number of sides of polygon.
n=int(input("\nEnter the number of sides polygon has :- "))
# Taking user input to get the length of each side of polygon.
s=float(input("\nEnter the length of each side of polygon :- "))

# Calculating the area of the polygon.
area=(n*s**2)/(4*math.tan(math.pi/n))

# Displaying results
print(f"\nArea of the polygon of {n} number of side and each of length {s} is = {round(area,2)}\n")