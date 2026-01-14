'''Q22:-In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area = s × (s − s1) × (s − s2) × (s − s3)
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.'''

"""
Summary:- Calculating area of a triangle by using heron's formula, where all sides of a triangle are known. 
"""
# Importing math module because we have to take square root in our calculation
import math

# Taking user input for side 1
s1=float(input("\nEnter the measurement of side 1 of a triangle :- "))
# Taking user input for side 2
s2=float(input("\nEnter the measurement of side 2 of a triangle :- "))
# Taking user input for side 3
s3=float(input("\nEnter the measurement of side 3 of a triangle :- "))

# This is semi-perimeter of a triangle
s=(s1+s2+s3)/2

# Calculating are of a trianglke using "HERON'S FORMULA"
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

# Displaying output
print(f"\nArea of a triangle whose side are known, using \'HERON'S FORMULA\' \n\
sides are s1={s1},s2={s2},s3={s3}\n\
\nArea of a triangle is = {round(area,2)}\n")