'''Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.'''

"""
Summary:-converting height unit in feet and inches into centimeters.
"""

print("\nEnter your height first in feet then in inches :- \n")
# Taking user input first in feet then in inches
height_feet=int(input("Enter your height in feet :- "))
height_inches=int(input("Enter your height in inches :- "))

# converting feet and inches into centimeters
height_cm=height_feet*12*2.54+height_inches*2.54

# Displaying the result
print(f"height of a person i.e {height_feet} feet and {height_inches} inches in centimeters = {height_cm} centimeters")
