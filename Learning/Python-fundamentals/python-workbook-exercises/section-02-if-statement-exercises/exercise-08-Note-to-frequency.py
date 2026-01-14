'''Q8:-The following table lists an octave of music notes, beginning with middle C, along
with their frequencies

Note    Frequency (Hz)

C4        261.63
D4        293.66
E4        329.63
F4        349.23
G4        392.00
A4        440.00
B4        493.88

Begin by writing a program that reads the name of a note from the user and
displays the note's frequency. Your program should support all of the notes listed
previously.
Once you have your program working correctly for the notes listed previously you
should add support for all of the notes from C0 to C8. While this could be done by
adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. Instead, you should
exploit the relationship between notes in adjacent octaves. In particular, the frequency
of any note in octave n is half the frequency of the corresponding note in octave n+1.
By using this relationship, you should be able to add support for the additional notes
without adding additional cases to your if statement.'''
"""
Summary:- This program tells the frequency of the notes entered 
"""

print("\nThis program tell the frequency of the notes entered\n")
# Displaying user about the range of octave supported by this program]
print("\nThis program supports all the notes from c0 to c8\n")
# Taking user input for note
n=input("\nPlease enter the note u want to check :- \n")

# Slicing the string to separate the note and octave
L=str.__len__(n)  

k=n[0]

try:

    o = int(n[1])

except ValueError:
    
    print("\nINVALID INPUT: Please enter a note in the correct format (e.g., c4, d5, etc.)\n")
    exit()



# ERROR HANDLING: what if user inputs notes such as c45, b4567 etc 
if(L>2):
        print("\nINVALID INPUT:This program supports only notes of octave number 0 to 8\n")

if(L<=2):

# ERROR HANDLING: what if user inputs out of this range of 0 to 8 octave 
    if((o<0 or o>8)):
        print("\nINVALID INPUT:This program supports only notes of octave number 0 to 8\n")

        
# displaying notes and frequecy mentioned in the table i.e [C4,D4,E4,F4,G4,A4,B4] 
    elif((k=='c' or k=='C') and o==4):
        print(f"\nFrequency of the note {k}{o} is = 261.63\n")
    elif((k=='d' or k=='D') and o==4):
        print(f"\nFrequency of the note {k}{o} is = 293.66\n")
    elif((k=='e' or k=='E') and o==4):
        print(f"\nFrequency of the note {k}{o} is = 329.63\n")
    elif((k=='f' or k=='F') and o==4):
        print(f"\nFrequency of the note {k}{o} is = 349.23\n")
    elif((k=='g' or k=='G') and o==4):
        print(f"\nFrequency of the note {k}{o} is = 392.00\n")
    elif((k=='a' or k=='A') and o==4):
        print(f"\nFrequency of the note {k}{o} is = 440.00\n")
    elif((k=='b' or k=='B') and o==4):
        print(f"\nFrequency of the note {k}{o} is = 493.88\n")

# Calculation of C note octave range from C0 to C8
    elif((k=='C' or k=='c') and o<4):
        r=4-o
        f=261.63/(r*2)# going octave lower than 4 each octave frequency is half of the previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    elif((k=='C' or k=='c') and o>4):
        r=o-4
        f=261.63*r*2 # while going octave greater than 4 each octave frequency is double of previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")

# Calculation of D note octave range from D0 to D8
    elif((k=='D' or k=='d') and o<4):
        r=4-o
        f=293.66/(r*2)# going octave lower than 4 each octave frequency is half of the previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    elif((k=='D' or k=='d') and o>4):
        r=o-4
        f=293.66*r*2 # while going octave greater than 4 each octave frequency is double of previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")

# Calculation of E note octave range from E0 to E8
    elif((k=='E' or k=='e') and o<4):
        r=4-o
        f=329.63/(r*2)# going octave lower than 4 each octave frequency is half of the previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    elif((k=='E' or k=='e') and o>4):
        r=o-4
        f=329.63*r*2 # while going octave greater than 4 each octave frequency is double of previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")

# Calculation of F note octave range from F0 to F8
    elif((k=='F' or k=='f') and o<4):
        r=4-o
        f=349.23/(r*2)# going octave lower than 4 each octave frequency is half of the previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    elif((k=='F' or k=='f') and o>4):
        r=o-4
        f=349.23*r*2 # while going octave greater than 4 each octave frequency is double of previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")

# Calculation of G note octave range from G0 to G8
    elif((k=='G' or k=='g') and o<4):
        r=4-o
        f=392.00/(r*2)# going octave lower than 4 each octave frequency is half of the previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    elif((k=='G' or k=='g') and o>4):
        r=o-4
        f=392.00*r*2 # while going octave greater than 4 each octave frequency is double of previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")

# Calculation of A note octave range from A0 to A8
    elif((k=='A' or k=='a') and o<4):
        r=4-o
        f=440.00/(r*2)# going octave lower than 4 each octave frequency is half of the previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    elif((k=='A' or k=='a') and o>4):
        r=o-4
        f=440.00*r*2# while going octave greater than 4 each octave frequency is double of previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")

# Calculation of B note octave range from B0 to B8
    elif((k=='B' or k=='b') and o<4):
        r=4-o
        f=493.88/(r*2) # going octave lower than 4 each octave frequency is half of the previous one 
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    elif((k=='B' or k=='b') and o>4):
        r=o-4
        f=493.88*r*2 # while going octave greater than 4 each octave frequency is double of previous one
        print(f"\nthe frequency of the note {k}{o} is = {f}\n")
    else:
        print("\nINVALID INPUT\n")
