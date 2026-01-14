'''Q7:-A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.'''

"""
Summary :- This program checks whether a triangle is an equilateral, isosceles or a scalene triangle.
"""

# Displaying objective of this program to user
print("\nThis program checks whether a triangle is an equilateral, isosceles or a scalene triangle.\n")

print("\nPlease enter the sides of the triangle :- ")

# Taking user input for the sides of the triangle
s1=float(input("Please enter the side 1 of the triangle :- "))
s2=float(input("Please enter the side 2 of the triangle :- "))
s3=float(input("Please enter the side 3 of the triangle :- "))

if(s1<=0 or s2<=0 or s3<=0):
    print("\nINVALID INPUT: sides of a triangle can't be negative or of a zero length\n")
elif(s1==s2==s3):
    print("\nAll 3 sides of an equilateral triangle have the same length\n")
    print(f"\nHence triangle of sides {s1}, {s2}, {s3} is an equilateral triangle\n")
elif(s1==s2 or s1==s3 or s2==s3):
    print("\nIn an isosceles triangle any two sides are of same length\n")
    print(f"\nHence triangle of sides {s1}, {s2}, {s3} is an isosceles triangle\n")
else:
    print("\nA scalene triangle is an triangle in which all of the sides are of different length\n")
    print(f"\nHence triangle of sides {s1}, {s2}, {s3} is an scalene triangle\n")