'''Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula:
BMI =weight/(height * height)* 703.
If you read the height in meters and the weight in kilograms then body mass index
is computed using this slightly simpler formula:
BMI =weight/(height * height)'''

"""
Summary:- This program calculates the BMI(body mass index) of an individual
"""
# Asking user to enter height of an individual
h=float(input("\nEnter the height of the individual either in inches or in meters :- "))

# Asking user to enter weight of an individual
w=float(input("\nEnter the weight of an individual either in pounds or in kilograms :- "))

# Checking the units of the user input
n=int(input("\nPlease press 1 if you have enetered height in inches and weight in pounds :- \
\nPlease press 2 if you have enetered height in metrs and weight in kilograms :- "))

if(n==1):
    BMI=w/(h*h)*703
    print(f"\nBMI(body mass index) of an individual of height {h} inches and weight {w} pounds is = {round(BMI,2)} lb/in^2")

elif(n==2):
    BMI=w/(h*h)
    print(f"\nBMI(body mass index) of an individual of height {h} meters and weight {w} kilograms is = {round(BMI,2)} kg/m^2")

else:
    print("\nINVALID INPUT\n")

# Greeting message
print("\nBE HEALTHY AND CHEERFUL :)")