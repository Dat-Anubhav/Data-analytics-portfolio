'''Q19:-In the previous exercise you created a program that converts a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ for a 4.0 (or greater) grade point average.'''

# Displaying the objective of this program to user
print("\nThis programs tells the letter grade if u enter the grade points\n")

try:
    
    # Taking user input
    p=float(input("\nPlease enter the grade points :- "))
except ValueError:
    print("\nINALID INPUT: Please enter the grade points in correct format (ex: 4.0, 4.6, 3.6 etc)\n")
    exit()

# Verifying the range for the entered grade points
if(p==4.0):

    print(f"\nThe letter grade equivalent to a grade point {p} is an A grade.\n")

elif(p>4.0):
    
    print(f"\nThe letter grade equivalent to a grade point {p} is an A+ grade.\n")

elif(p>=3.7 and p<4.0):

    print(f"\nThe letter grade equivalent to a grade point {p} is an A- grade.\n")

elif(p>=3.3):

    print(f"\nThe letter grade equivalent to a grade point {p} is an B+ grade.\n")

elif(p==3.0 and p<3.3):

    print(f"\nThe letter grade equivalent to a grade point {p} is an B grade.\n")

elif(p>=2.7 and p<3.0):

    print(f"\nThe letter grade equivalent to a grade point {p} is an B- grade.\n")

elif(p>=2.3):

    print(f"\nThe letter grade equivalent to a grade point {p} is an C+ grade.\n")

elif(p==2.0 and p<2.3):

    print(f"\nThe letter grade equivalent to a grade point {p} is an C grade.\n")

elif(p>=1.7 and p<2.0):

    print(f"\nThe letter grade equivalent to a grade point {p} is an C- grade.\n")

elif(p>=1.3):

    print(f"\nThe letter grade equivalent to a grade point {p} is an D+ grade.\n")

elif(p==1.0 and p<1.3):

    print(f"\nThe letter grade equivalent to a grade point {p} is an D grade.\n")

elif(p==0 and p<1.0):

    print(f"\nThe letter grade equivalent to a grade point {p} is an F grade (FAIL).\n")

else:

    print("\nThis grading system does not include any negative grading points.\n")