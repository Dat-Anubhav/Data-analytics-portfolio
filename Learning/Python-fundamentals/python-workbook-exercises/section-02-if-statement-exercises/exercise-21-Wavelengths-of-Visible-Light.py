'''Q21:-The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Color       Wavelength (nm)

Violet      380 to less than 450
Blue        450 to less than 495
Green       495 to less than 570
Yellow      570 to less than 590
Orange      590 to less than 620
Red         620 to 750

Write a program thatreads a wavelengthfrom the user andreports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.'''

# Displaying the objective of this program to user
print("\nThis program determines the color of visible light based on the wavelength you enter.\n")

try:

    # Taking user input
    w=float(input("Please enter the wavelength of the visible light (in nonometers) you would like to check:- "))
except ValueError:
    print("\nINVALID INPUT: Pleae enter in correct format (ex: 400, 500, 650 etc)\n")
    exit()

if(w>=380 and w<450):
    
    print(f"\nThe color of the light with wavelength {w} is = VIOLET \n")

elif(w>=450 and w<495):

    print(f"\nThe color of the light with wavelength {w} is = BLUE \n")

elif(w>=495 and w<570):

    print(f"\nThe color of the light with wavelength {w} is = GREEN \n")

elif(w>=570 and w<590):

    print(f"\nThe color of the light with wavelength {w} is = YELLOW \n")

elif(w>=590 and w<620):

    print(f"\nThe color of the light with wavelength {w} is = ORANGE \n")

elif(w>=620 and w<750):

    print(f"\nThe color of the light with wavelength {w} is = RED \n")

else:

    print("\nINVALID INPUT: The wavelength of visible light ranges from 380 to 750 nanometers (nm).\n")
