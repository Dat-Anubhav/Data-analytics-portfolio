'''Q16:-The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:

Magnitude               Descriptor
Less than 2.0           Micro

2.0 to less than 3.0    Very minor
3.0 to less than 4.0    Minor
4.0 to less than 5.0    Light
5.0 to less than 6.0    Moderate
6.0 to less than 7.0    Strong
7.0 to less than 8.0    Major
8.0 to less than 10.0   Great
10.0 or more            Meteoric

Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.'''

"""
Summary:- If user inputs the magnitude of earthquake 
this program tells the magnitude range on the Richter scale and its description  
"""

# Displaying objective of this program
print("\nThis program tells the earthquake magnitude ranges on the Richter scale and their descriptors\n")

# ERROR HANDLING: if user input a string then this try except block will prevent the program from crashing
try:

    # Taking user input
    m=float(input("\nPlease enter the earthquake's magnitude :- "))
except ValueError:
    print("\nINVALID INPUT: Please enter the input in correct format (ex: 2.0, 4.0, 7.7 etc)\n")
    exit()
# Checking conditions for different earthquake magnitudes 
if(m<2.0):
    print(f"\nEarthquake of {m} magnitude is a MICRO earthquake\n")
elif(m>=2.0 and m<3.0):
    print(f"\nEarthquake of {m} magnitude is a VERY MINOR earthquake\n")

elif(m>=3.0 and m<4.0):
    print(f"\nEarthquake of {m} magnitude is a MINOR earthquake\n")

elif(m>=4.0 and m<5.0):
    print(f"\nEarthquake of {m} magnitude is a LIGHT earthquake\n")

elif(m>=5.0 and m<6.0):
    print(f"\nEarthquake of {m} magnitude is a MODERATE earthquake\n")

elif(m>=6.0 and m<7.0):
    print(f"\nEarthquake of {m} magnitude is a STRONG earthquake\n")

elif(m>=7.0 and m<8.0):
    print(f"\nEarthquake of {m} magnitude is a MAJOR earthquake\n")

elif(m>=8.0 and m<10.0):
    print(f"\nEarthquake of {m} magnitude is a GREAT earthquake\n")

elif(m>=10.0):
    print(f"\nEarthquake of {m} magnitude is a METEORIC earthquake\n")
