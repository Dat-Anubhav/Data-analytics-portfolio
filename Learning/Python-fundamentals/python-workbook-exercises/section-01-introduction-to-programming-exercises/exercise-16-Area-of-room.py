'''Q16:- Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr2. The
volume of a sphere is computed using the formula volume = 4/3πr3'''

"""
Summary:- calculating area of acircle and volume of a sphere both of radius r using pi from math module.
"""


r=float(input("\nEnter the radius of a circle or a sphere :- "))

# importing math function use the exact value of pi
import math

# calculating area of a circle
area_circle=math.pi*r**2

# Calculating volume of a sphere
volume_sphere=4/3*math.pi*r**3

# Displaying results
print(f"\nRadius of a circle or sphere is = {r}\
\nArea of a circle = {area_circle}\nVolume of a sphere = {volume_sphere}\n")

# To access the mathematical constant pi in Python, the math module can be utilized.
# The math module in Python is a built-in library that provides access to a wide range
# of standard mathematical functions and constants
# widely used in scientific computing, data analysis, engineering, and other fields