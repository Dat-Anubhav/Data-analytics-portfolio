'''Q5:-The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.'''

"""
Summary:- This program tell the number of days in a month.
"""
# Displaying the objective of this program
print("\nThis program tell the number of days in a month.\n")

# Taking user input
n=input("\nPlease enter the full name of the month(no short forms) which you want check :- ")

# checking conditions for the months which have only 30 days and also checking the all possible cases of input
if (n=="APRIL" or n=="April" or n=="april" or n=="JUNE" or n=="June" 
or n=="june" or n=="AUGUST" or n=="August" or n=="august" or n=="OCTOBER" or n=="October" or n=="october" or
n=="DECEMBER" or n=="December" or n=="december"):
            
        print(f"\n{n} month contains 30 days\n")

# separate condition for february because it has 28 days in a normal year and 29 days in a leap year.
elif(n=="FEBRUARY" or n=="February" or n=="february"):
        
        print(f"\n{n} month contains 28 days and 29 days in a leap year\n")
# rest of the months like jan ,mar , may etc have 31 days
elif(n=="JANUARY" or n=="January" or n=="january" or n=="MARCH" or n=="March" or n=="march" or n=="MAY" or n=="May" or n=="may"
or n=="JULY" or n=="July" or n=="july" or n=="SEPTEMBER" or n=="September" or n=="september" or n=="NOVEMBER" or n=="November"
or n=="november"):
        print(f"\n{n} months contains 31 days\n")

# ERROR HANDLING: What if userinputs short form of months or any other random input
else:
        print("\nINVALID INPUT\n")

# Greeting message
print("\nHAVE A NICE DAY :)\n")