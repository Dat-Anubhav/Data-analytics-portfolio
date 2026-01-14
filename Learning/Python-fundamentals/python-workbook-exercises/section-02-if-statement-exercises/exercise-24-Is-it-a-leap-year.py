'''Q24:-Most years have 365 days. However, the time required for the Earth to orbit the Sun
is actually slightly more than that. As a result, an extra day, February 29, is included
in some years to correct for this difference. Such years are referred to as leap years.
The rules for determining whether or not a year is a leap year follow:

• Any year that is divisible by 400 is a leap year.
• Of the remaining years, any year that is divisible by 100 is not a leap year.
• Of the remaining years, any year that is divisible by 4 is a leap year.
• All other years are not leap years

Write a program that reads a year from the user and displays a message indicating
whether or not it is a leap year.'''

# Displaying objective of this program
print("\nThis program checks whether the entered year is a leap year.\n")

# The try except block prevents the program from crashing: what if user entered float or string value
try:

    # Taking user input
    y=int(input("\nPlease enter the year u want to check :- "))
except ValueError:
    print("\nINVALID INPUT: Please enter the correct format (ex: 20011, 2024, 1978 etc )\n")
    exit()

# Checking conditions for a leap year 
if(y%400==0):
    
    print(f"\nEntered year {y} is a leap year. \n")

elif(y%100==0):

    print(f"\nEntered year {y} is not a leap year. \n")

elif(y%4==0):

    print(f"\nEntered year {y} is a leap year. \n")

else:

    print(f"\nEntered year {y} is not a leap year. \n")