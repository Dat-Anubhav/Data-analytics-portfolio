'''In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG).
 In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.'''

"""
Summary :- To know the fuel efficiency of an U.S vehicle in canada
"""


# taking user input
us=float(input("\nenter the fuel effeciency in miles per gallon(MPG) :- "))
print(f"\nyour fuel efficiency in U.S units i.e miles per gallon(MPG) is = {us} (Miles-per-Gallon)\n")

#  MPG i s a standard in U.S to define the fuel efficiency of a vehicle
#  to know the fuel efficiency in canadian units we have to convert it into litres per 100 km(L/100 km)

# U.S unit is in miles per gallon we have to convert it into km per litre and then we will convert it into L/100km (reciprocal)

# as we know that "1 mile=1.60934 km and 1 gallon=3.78541 liters"
canada=us*1.60934 # converting miles to km (this is in km per galoon) [UNIT:-KM/GALLON]

canada=canada/3.78541 # this is in km in 3.78541 litres (converting galons to litres) [UNIT:-KM/LITRES]

# since 1 gallon=3.78541 litres basically in this step we are converting gallons into litres
# our canada variable holding the value in km per 3.78541 litres for now we have to convert it into 1L per 100 km(L/100km)


canada= 1/canada*100 # converting it into 1 litre per 100 km, reciprocal and multiplying by 100 to make it in (L/100km)
print(f"fuel efficiency of your vehicle in canada i.e is in (L/100km) = {canada} (Litres/100kilometers)\n")