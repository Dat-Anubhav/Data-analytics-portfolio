'''Q2:-It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.'''

"""
Summary:- This program converts human years into equivalent dog years
"""
print("\nThis program converts human years into equivalent dog years\n")

h=float(input("\nPlease enter the human years :- "))

if(h<0):
    # ERROR Handling : What if user inputs human years in negative; as we know human years can't be in negative
    print("\nINVALID INPUT human years can't be in negative")

elif(h<=2):
    # since for first to 2 year of human is = 10.5 years of a dog
    d=h*10.5
    # Displaying results
    print(f"\n{h} Human years equivalent to {d} Dog years\n")

else:
    # Calculating dog years for more than 2 years of human
    d=2*10.5+((h-2)*4)
    # Displaying results
    print(f"\n{h} Human years equivalent to {d} Dog years\n")

