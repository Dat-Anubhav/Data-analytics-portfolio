'''Q6:-The following table lists the sound level in decibels for several common noises

Noise Decibel level     (dB)

Jackhammer              130
Gas lawnmower           106
Alarm clock             70
Quiet room              40

Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table'''

"""
Summary:- This program checks and tells the noise decibels level of places or objects.
"""

# Displaying the objective of the program
print("\nThis program checks and tells the noise decibels level of places or objects \n")
# Taking user input
d=float(input("\nPlease enter the sound levels in decibels :- "))

# Checking all the possible conditions
if(d==40):
    print("\nThis is quiet room noise decibel level\n")
elif(d==70):
    print("\nThis is alarm clock noise decibel level\n")
elif(d==106):
    print("\nThis is gas lawnmower noise decibel level\n")
elif(d==130):
    print("\nThis is jackhammer noise decibel level\n")
elif(d>40 and d<70):
    print("\nThis comes in a range of a quiet room and alarm clock noise decibel level\n")
elif(d>70 and d<106):
    print("\nThis comes in a range of an alarm clock and gas lawnmower noise decibel level\n")
elif(d>106 and d<130):
    print("\nThis comes in a range of a gas lawnmower and a jackhammer noise decibel level\n")
elif(d>130):
    print("\nThis is above jackhammer noise decibel level\n")
elif(d<40):
    print("\nThis is below quiet room noise decibel level\n")