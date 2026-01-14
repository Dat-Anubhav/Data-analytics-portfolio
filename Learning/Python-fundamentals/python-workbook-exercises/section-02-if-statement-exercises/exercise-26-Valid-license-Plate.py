'''Q26:-In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three numbers. When all of the license plates following that pattern had
been used, the format was changed to four numbers followed by three uppercase
letters.
Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate.'''

# Displaying the objective of this program
print("\nThis program checks the license plate style\n")

# Taking user input 
lp=input("\nPlease enter your license plate :- \n")

# Calculating the length of the string to differentiate between older and newer styles. 
len=str.__len__(lp)

# Providing information on the formats of older and newer style license plates.
print("\nIn a particular jurisdiction, older license plates consist of three uppercase letters\
 followed by three numbers.")

print("\nIn newer style license plate the format was changed to four numbers followed by three uppercase \
letters.\n")

# Checking conditions for older style license plates
if(len==6):

    try:
        
        o1=bool(((lp[0].upper()==lp[0])))
        o2=bool(((lp[1].upper()==lp[1])))
        o3=bool(((lp[2].upper()==lp[2])))
        o4=bool((int(lp[3])))
        o5=bool((int(lp[4])))
        o6=bool((int(lp[5])))
    except ValueError:
        print("\nINVALID LICENSE PLATE: Please enter the correct format\n")
        exit()

    
    if(o1==True and o2==True and o3==True and o4==True and o5==True and o6==True):

        print(f"\nYour license plate {lp} is an older style license plate\n")

    else:
        
        print("\nInvalid license plate\n")

# Checking conditions for newer style license plates    
elif(len==7):

    try:

        k1=bool((int(lp[0])))
        k2=bool((int(lp[1])))
        k3=bool((int(lp[2])))
        k4=bool((int(lp[3])))
        k5=bool(((lp[4].upper()==lp[4])))
        k6=bool(((lp[5].upper()==lp[5])))
        k7=bool(((lp[6].upper()==lp[6])))

    except ValueError:
        print("\nINVALID LICENSE PLATE: Please enter the correct format\n")
        exit()

    if(k1==True and k2==True and k3==True and k4==True and k5==True and k6==True):

        print(f"\nYour license plate {lp} is an newer style license plate\n")

    else:
        print("\nInvalid license plate\n")
# ERROR HANDLING: What if the user inputs a very long or very short string
else:
    print("\nINVALID INPUT\n")

print("\nThank you for using the license plate checker. Drive safely!\n")


