'''Q4:-Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.'''

"""
Summary:- This program can tell name of that shape by entering its number of sides
"""
# Displaying user objective of this program
print("\nThis program can tell name of that shape by entering its number of sides \n")
# Taking user input
s=int(input("\nPlease enter the number of sides from 3 to 10 :- "))

# Checking conditions 
if(s==3):
    print("\nIt's a triangle\n")
elif(s==4):
    print("\nIt's a quadrilateral\n")
elif(s==5):
    print("\nIt's a pentagon\n")
elif(s==6):
    print("\nIt's a hexagon\n")
elif(s==7):
    print("\nIt's a heptagon(also known as septagon)\n")
elif(s==8):
    print("\nIt's a octagon\n")
elif(s==9):
    print("\nIt's a nonagon\n")
elif(s==10):
    print("\nIt's a decagon\n")
else:
    
    # Appropriate error message for when the number of sides entered is outside the range of 3 to 10
    print("\nINVALID INPUT\n")