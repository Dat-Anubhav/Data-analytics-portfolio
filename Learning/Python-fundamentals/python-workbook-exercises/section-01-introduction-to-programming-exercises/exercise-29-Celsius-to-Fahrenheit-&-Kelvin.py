'''Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.'''

"""
Summary:- This program converts degree celsius into different scales
"""
# Displaying user what this program is about
print("\nThis program converts degree celsius into different scales\n")

# Taking user input for degree celsius
c=float(input("\nEnter the temperature in degree celsius :- "))

#Displaying the different scales into which this program can convert degree celsius 
print("\nMost commonly used temperature units or scales are degree celsius , degree fahrenheit , and Kelvin \
other less used units or Scales are degree Newton and degree rankine ")

j=int(input("\nPress 1 to convert degree celsius to degree Fahrenheit\n \
 Press 2 to convert degree celsius to Kelvin \n\
 Press 3 to convert degree celsius to degree Newton \n\
 Press 4 to convert degree celsius to degree Rankine :- \n"))

# Converting degree celsius into respective scales also diplaying results upto 2 decimal places.
if(j==1):

    # Converting degree celsius to degree Fahrenheit
    f=c*1.8+32
    print(f"\nEntered temperature is in degree celsius :- {c}\n \
      \nequivalent temperature in degree Fahrenheit = {round(f,2)}\n")

elif(j==2):

    # Convrting degree celsius to Kelvin
    k=c+273.15
    print(f"\nEntered temperature is in degree celsius :- {c}\n \
      \nequivalent temperature in Kelvin = {round(k,2)}\n")

elif(j==3):

    # Converting degree celsius to degree Newton
    n=c*33/100
    print(f"\nEntered temperature is in degree celsius :- {c}\n \
      \nequivalent temperature in degree Newton = {round(n,2)}\n")

elif(j==4):

    # Converting degree celsius to degree Rankine
    r=1.8*(c+273.15)
    print(f"\nEntered temperature is in degree celsius :- {c}\n \
      \nequivalent temperature in degree Rankine ={round(r,2)} \n")
else:
    print("\nINVALID INPUT\n")


