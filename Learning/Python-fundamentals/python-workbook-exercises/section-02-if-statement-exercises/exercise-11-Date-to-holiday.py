'''Q11:-Canada has three national holidays which fall on the same dates each year.

Holiday             Date

New year’s day     January 1
Canada day          July 1
Christmas day      December 25

Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.'''

# Displaying the objective of the program
print("\n This program checks the fixed National Holidays for the entered month and date\n")

# Taking user input for the  month and date
print("\nPlease enter the month and date to check the whether their is a national holiday or not :-  \n")
try:

# Taking user input for date
    d=int(input("\nPlease enter the date :- \n"))
except ValueError:
    print("\nINVALID INPUT: Please enter the valid date and month format\n")
    exit()
# Taking user input for the month
m=input("\nPlease enter the month :-\n")
if(d==1 and (m=="JANUARY" or m=="January" or m=="january")):
    print(f"\n{d} {m} = canada's New year day and its a fixed National Holiday in Canada\n")

elif(d==1 and (m=="JULY" or m=="July" or m=="july")):
    print(f"\n{d} {m} = canada day and its a fixed National Holiday in Canada\n")

elif(d==25 and (m=="DECEMBER" or m=="December" or m=="december")):
    print(f"\n{d} {m} = Christmas day and its a fixed National Holiday in Canada\n")

else:
    print("\nINVALID INPUT : OR there is no fixed National holiday in this month and date\n")