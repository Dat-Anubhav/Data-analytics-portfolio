'''When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in
degrees Fahrenheit and wind speeds in miles per hour.
WCI = 13.12 + 0.6215*Ta − 11.37*V 0.16 + 0.3965Ta*V 0.16
Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.

The wind chill index is only considered valid for temperatures less than or
equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
hour.'''

# Taking user input for temperature of air in degree celsius
ta=float(input("\nEnter the temperature in degree celsius :- "))

# Taking user input for velocity of air in kilometers per hour
v=float(input("\nEnter the velocity of the air in kilometers per hour :- "))

# Applying the conditions for WCI(Wind chill index)
if(ta<=10 and v>=4.8):

    # Calculating the wind chill index with the formula given below
    WCI=13.12+0.6215*ta-11.37*v*0.16+0.3965*ta*v*0.16

    # Displaying results
    print(f"\nThe Wind chill index of an air of temperature {ta} degree celsius and velocity {v} kilometers per hour is = {round(WCI,2)}\n")
else:
    
    print("\nYour inputs are not in range \n")
    # note:-
    print("\nNote:- The wind chill index is only considered valid for temperatures less than or equal to 10 degrees Celsius  \
and wind speeds exceeding 4.8 kilometers per hour\n")