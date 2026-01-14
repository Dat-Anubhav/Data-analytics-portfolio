'''Q9:-In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.'''

"""
Summary:- This program tells the note if u entered the frequency from the following table

Note    Frequency (Hz)
C4        261.63
D4        293.66
E4        329.63
F4        349.23
G4        392.00
A4        440.00
B4        493.88

"""
print("\nThis program tells the note if u entered the frequency from the following table\n\
      Note    Frequency (Hz)\n\
       C4        261.63\n\
       D4        293.66\n\
       E4        329.63\n\
       F4        349.23\n\
       G4        392.00\n\
       A4        440.00\n\
       B4        493.88\n")
# Taking user input
f=float(input("\nPlease enter the frequency you want to check :- \n"))
# checking conditions according to previous question table
if(f==261.63):
    print(f"\nThis frequency {f} belongs to C4 note \n")
elif(f==293.66):
    print(f"\nThis frequency {f} belongs to D4 note \n")
elif(f==329.63):
    print(f"\nThis frequency {f} belongs to E4 note \n")
elif(f==349.23):
    print(f"\nThis frequency {f} belongs to F4 note \n")
elif(f==392.00):
    print(f"\nThis frequency {f} belongs to G4 note \n")
elif(f==440.00):
    print(f"\nThis frequency {f} belongs to A4 note \n")
elif(f==493.88):
    print(f"\nThis frequency {f} belongs to B4 note \n")
else:
    print("\nNO RESULTS\n")