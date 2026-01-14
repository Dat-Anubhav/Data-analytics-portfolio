'''Q12:-Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below:

Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking.'''
"""
Summary:- This program tell the color of the chess board block entered 
"""
# Displaying objective of this program
print("\nThis program tell the color of the chess board block entered \n")
# Taking user input
p=input("please enter the position u want to check :- ")

# Finding the length of the string to check the correct format such as a1,b7,g8 of 8*8 size chess board
len=str.__len__(p)
# Checking the format of the input
if(len<2 or len>2):
    print("\nINVALID INPUT: Please enter the correct format (ex: a1,b2,c1 etc) of 8*8 chess board size\n")
    exit() # if input is in wrong format then this exit() function stops the further calculations done by the interpretor
# Checking required length i.e 2 ex: a2,c5,b8 etc
elif(len==2):
    # through string slicing extracted the co-ordinates of the block (column and row of the chess board)
    a=p[0]
    try:

        n=int(p[1])
    except ValueError:
        print("\nINVALID INPUT : Please enter the valid format (EX: A1, b2, g5 etc ) \n")
        exit()

if(a=='a' or a=='A'):
    # if 1 block is black then another one is white and then next another one is black ad so on means at odd even places
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is black\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is white\n")

elif(a=='b' or a=='B'):
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is white\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is black\n")

elif(a=='c' or a=='C'):
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is black\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is white\n")

elif(a=='d' or a=='D'):
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is white\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is black\n")

elif(a=='e' or a=='E'):
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is black\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is white\n")

elif(a=='f' or a=='F'):
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is white\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is black\n")

elif(a=='g' or a=='G'):
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is black\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is white\n")

elif(a=='h' or a=='H'):
    if(n%2!=0):# at odd place
        print(f"\nColor of the block {a}{n} is white\n")
    else:# at even place
        print(f"\nColor of the block {a}{n} is black\n")

# ERROR HANDLING: what if user inputs out of the range of a 8*8 size chess board such as m7 or k9 etc
else:
    print("\nINVALID INPUT\n")
