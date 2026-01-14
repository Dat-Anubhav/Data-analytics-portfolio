'''Q18:-At a particular university, letter grades are mapped to grade points in the following
manner

Letter Grade    points

A+              4.0
A               4.0
A−              3.7
B+              3.3
B               3.0
B−              2.7
C+              2.3
C               2.0
C−              1.7
D+              1.3
D               1.0
F                0

Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.'''

# Displaying the objective of the program
print("\nThis program tells the grade points if you enter the letter grade\n")

# Taking the user input
l=input("\nPlease enter the letter grade :- ")

# Converting the input character into uppercase such as A+, B, C- etc to reduce the conditions in if
L=l.upper()
# Finding the length of the string 
# To check the invalid inputs because Input can only consist of one or two characters.
len=str.__len__(L)

if(len==2):

    if(L[0]=='A' and L[1]=='+'):
    
        print(f"\nFor letter grade {l} grade points will be = 4.0\n")

    elif(L[0]=='A' and L[1]=='-'):
    
        print(f"\nFor letter grade {l} grade points will be = 3.7\n")

    elif(L[0]=='B' and L[1]=='+'):
    
        print(f"\nFor letter grade {l} grade points will be = 3.3\n")

    elif(L[0]=='B' and L[1]=='-'):
    
        print(f"\nFor letter grade {l} grade points will be = 2.7\n")

    elif(L[0]=='C' and L[1]=='+'):
    
        print(f"\nFor letter grade {l} grade points will be = 2.3\n")

    elif(L[0]=='C' and L[1]=='-'):
    
        print(f"\nFor letter grade {l} grade points will be = 1.7\n")

    elif(L[0]=='D' and L[1]=='+'):
    
        print(f"\nFor letter grade {l} grade points will be = 1.3\n")
    else:
        print("\nINVALID INPUT\n")

elif(len==1):

    if(L[0]=='A'):

        print(f"\nFor letter grade {l} grade points will be = 4.0\n")
    
    elif(L[0]=='B'):

        print(f"\nFor letter grade {l} grade points will be = 3.0\n")

    elif(L[0]=='C'):

        print(f"\nFor letter grade {l} grade points will be = 2.0\n")
    
    elif(L[0]=='D'):

        print(f"\nFor letter grade {l} grade points will be = 1.0\n")
    
    elif(L[0]=='F'):

        print(f"\nFor letter grade {l} grade points will be = 0\n")
    
    else:
        print("\nINVALID INPUT\n")
# ERROR HANDLING
else:
    print("INVALID INPUT : Please input in correct format (ex: A+, a-, a, B, B+ etc)")


    