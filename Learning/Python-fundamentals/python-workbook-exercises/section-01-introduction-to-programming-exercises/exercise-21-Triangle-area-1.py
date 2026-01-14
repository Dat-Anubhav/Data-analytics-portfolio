'''Q21:-The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area =(b * h)/2
Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base length b and height h.'''

"""
Summary:- Calculating the area of a triangle and displaying it along with its base and height. 
"""

# Taking user input for the base of the triangle. 
b=float(input("\nEnter the base of the triangle :- "))

#Taking user input for the height of the triangle. 
h=float(input("\nEnter the height of the triangle :- "))

# Calculating area of triangle
a=b*h

# Displaying results
print(f"\nArea of the triangle of base {b} and of height {h} is = {a} \n")