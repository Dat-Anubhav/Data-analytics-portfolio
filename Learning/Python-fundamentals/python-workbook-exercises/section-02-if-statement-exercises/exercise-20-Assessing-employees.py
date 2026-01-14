'''Q20:-At a particular company, employees are rated at the end of each year. The rating scale
begins at 0.0, with higher values indicating better performance and resulting in larger
raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
with each rating is shown in the following table. The amount of an employee's raise
is $2400.00 multiplied by their rating.

Rating Meaning
0.0 Unacceptable performance
0.4 Acceptable performance
0.6 or more Meritorious performance

Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s
raise should also be reported. Your program should display an appropriate error
message if an invalid rating is entered.'''

# Displaying objective of this program
print("\nThis program calculates employee raises and performance based on their ratings.\n")

# Preventing the program from crashing: what if the user enters an invalid input format, such as ifhef or one, two, etc
try:
    # Taking user input
    r=float(input("\nPlease enter the rating of an employee :- \n"))
except ValueError:
    print("\nINVALID INPUT: Please enter the valid format (ex: 0.4, 0.6, 0.8 etc)\n")
    exit()

# Checking conditions 
if(r==0.0):

    print(f"\nEmployee of a rating {r} has a Unacceptable performance\n\
The amount of employee raise = ${r*2400}\n")

elif(r==0.4):

    print(f"\nEmployee of a rating {r} has a Acceptable performance\n\
The amount of employee raise = ${r*2400}\n")

elif(r>=0.6):

    print(f"\nEmployee of a rating {r} has a Meritorious performance\n\
The amount of employee raise = ${r*2400}\n")

else:

    print("INVALID INPUT: The value awarded to an employee is either 0.0, 0.4, or 0.6 or more")