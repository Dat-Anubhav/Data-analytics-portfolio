# A function to convert temperature between Celsius and Fahrenheit.
def temperature_conversion(temp,unit):

# Check if the unit is Celsius (either lower or upper case)
    if (unit=='c' or unit=='C'):
        
        print("\nCelsius to Fahrenheit\n")

# Convert Celsius to Fahrenheit using the formula (C × 9/5) + 32
        return (temp*9/5 +32) 
    
# Check if the unit is Fahrenheit (either lower or upper case)
    if(unit=='f' or unit=='F'):
        print("\nFahrenheit to Celsius\n")

# Convert Fahrenheit to Celsius using the formula (F − 32) × 5/9
        return ((temp-32)*5/9)
    
    # If the unit is not recognized, return None
    else:

        return None

# Example: Convert 76 Fahrenheit to Celsius
print(temperature_conversion(76,'f'))
# Example: Convert 22.5 Celsius to Fahrenheit
print(temperature_conversion(22.5,'C'))
