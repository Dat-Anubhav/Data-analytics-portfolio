'''Q13:-The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise:

Season      First day

Spring      March 20
Summer      June 21
Fall        September 22
Winter      December 21

Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered.'''

"""
Summary:- This program tells the season if u enter a month name and a date 
"""
# Displaying objective of this program
print("\nThis program tells the season if u enter a month name and a date\n")

# Taking user input for month name
m=input("\nPlease enter the month:- ")

try:
# Taking user input for the date
    d=int(input("\nPlease enter the date :- "))
except ValueError:
    print("\nINVALID INPUT : Please enter the valid format (march 21, DECEMBER 24, July 26 etc ) \n")
    exit()
# Capitalizing all the characters of the month string to reduce the number of if conditions
M=m.upper()

# Checking for winter months
if(M=="DECEMBER" or M=="JANUARY" or M=="FEBRUARY" or M=="MARCH"):
    
    if(M=="DECEMBER" and d<21):
        print(f"\n{m}{d} comes in Falls season\n")
    
    if(M=="MARCH" and d>=20):
        print(f"\n{m}{d} comes in Spring season\n")
    else:
        print(f"\n{m}{d} comes in Winter season\n")
# Checking for spring months
elif(M=="APRIL" or M=="MAY" or M=="JUNE" or M=="MARCH"):

    if(M=="JUNE" and d>=21):
        print(f"\n{m}{d} comes in Summer season\n")
    
    else:
        print(f"\n{m}{d} comes in spring season\n")

# Checking for summer months
elif(M=="JUNE" or M=="JULY" or M=="AUGUST" or M=="SEPTEMBER"):

    if(M=="SEPTEMBER" and d>=22):
        print(f"\n{m}{d} comes in Fall season\n")
    else:
        print(f"\n{m}{d} comes in Summer season\n")

# ERROR HANDLING: what if user input short form og month name or any other irrelevant 
else:
    print("\nINVALID INPUT\n")
