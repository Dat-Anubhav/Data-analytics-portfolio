'''Q20:-The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 J
mol K, and T is the
temperature in degrees Kelvin.
Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit'''

"""
Summary:- Calculating the amount of gas a SCUBA tank has in no of moles using Ideal Gas Law.
"""

# Taking user input for pressure of gas
p=float(input("\nEnter the pressure of gas in pascals :- "))

# Tkaing user input for volume of gas
v=float(input("\nEnter the volume of gas in liters :- "))

# Taking user input for the temperature of the gas
t=float(input("\nEnter the temperature of the gas in degree celsius or in fahrenheit :- "))

check=int(input("\nPlease press 1 if you have entered the temperature in degree celsius \n\
or Press 2 if you have entered the temperature in degree fahrenheit :-  "))

# R is the ideal gas constant = 8.314 J/mol*k
R=8.314

# if entered temperature is in degree celcius. 
kct=t+273.15

# If the entered temerature is in degree fahrenheit
# to convert fahrenheit into kelvin.

kft=t-32*5/9+273.15 

#to change fahrenheit into degree celcius just dont add 273.15.

# Calculating the amount of gas in (n) number of moles.

if(check==1):
    
    n=p*v/R*kct # Calculations if user has entered the temperature in degree celsius.

elif(check==2):
    
    n=p*v/R*kft # Calculattion if user has entered the temperature in degree fahrenheit.

else:
    
    print("\n'INVALID INPUT\'\n")

if(check==1):
    check="Degree Celsius"
elif(check==2):
    check="Degree Fahrenheit"

# Displaying output
print(f"\n The amount of gas in number of moles in a SCUBA tank \nof volume {v} ,pressure {p}, \
temperature {t} {check} is = {round(n,2)} moles\n")


