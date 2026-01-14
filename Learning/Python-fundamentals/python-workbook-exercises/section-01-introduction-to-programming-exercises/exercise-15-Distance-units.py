'''Q15:-In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.'''

"""
Summary :- converting measurement taken by the user in feet into inches,yards and miles.
"""

# Inches: 1 foot = 12 inches
# Yards: 1 foot = 1/3 yard (0.333...) i.e 1 yard = 3 feet
# Miles: 1 foot = 1/5,280 mile i.e 1 mile = 5280 feet

feet=int(input("Enter the measurement in feet :- "))

#converting feet into inches,yard and miles
inch=feet*12
yard=feet/3
mile=feet/5280

# Displaying results
print(f"provided measurement in feet = {feet} feet\nConversion in inches = {inch} inches\
\nConvertion in yards = {yard} yards\nConvertion in miles = {mile} miles")
#created f string to print the values
# \n to print in new line in output
# \ to split the long print statement