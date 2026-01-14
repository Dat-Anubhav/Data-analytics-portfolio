'''Q22:-Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Name                Frequency range (Hz)

Radio waves         Less than 3 × 10^9
Microwaves          3 × 10^9 to less than 3 × 10^12
Infrared light      3 × 10^12 to less than 4.3 × 10^14
Visible light       4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet light   7.5 × 10^14 to less than 3 × 10^17
X-rays              3 × 10^17 to less than 3 × 10^19
Gamma rays          3 × 10^19 or more

Write a program that reads the frequency of the radiation from the user and displays
the appropriate name.'''

# Displaying the objective of this program to user
print("\nThis program identifies the type of electromagnetic radiation when you enter its frequency.\n")

# try except block will prevent the program from crashing : what if user input in string
try:

    # Taking user input
    f=float(input("\nPlease enter the frequency of the radiation :- \n"))
except ValueError:
    print("\nINVALID INPUT: Please enter in corrct format\n")
    exit()

# ERROR HANDLING: if user input negative frequency
# The frequency of a real electromagnetic wave cannot be negative in a physical sense.
if(f<0):
    print("\nINVALID INPUT: The frequency of a real electromagnetic wave cannot be negative in a physical sense.\n")
    exit()

# Checking frequency range
if(f<3*(10**9)):

    print(f"\nElectromagnetic radiation of frequency {f} comes under RADIO WAVES\n")

elif(f>=3*(10**9) and f<3*(10**12)):

    print(f"\nElectromagnetic radiation of frequency {f} comes under MICRO WAVES\n")

elif(f>=3*(10**12) and f<4.3*(10**14)):

    print(f"\nElectromagnetic radiation of frequency {f} comes under INFRARED LIGHT\n")

elif(f>=4.3*(10**14) and f<7.5*(10**14)):

    print(f"\nElectromagnetic radiation of frequency {f} comes under VISIBLE LIGHT\n")

elif(f>=7.5*(10**14) and f<3*(10**17)):

    print(f"\nElectromagnetic radiation of frequency {f} comes under ULTRA-VIOLET LIGHT\n")

elif(f>=3*(10**17) and f<3*(10**19)):

    print(f"\nElectromagnetic radiation of frequency {f} comes under X-rays\n")

elif(f>=3*(10**19)):

    print(f"\nElectromagnetic radiation of frequency {f} comes under GAMMA rays\n")

else:

    print("\nINVALID INPUT\n")