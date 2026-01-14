'''Q12:- Define a recursive function that calculates the factorial of a given number. 
Test the function with different inputs.'''

# Defining a recursive function that calculates the factorial of a given number.
def factorial(n):

    if (n==0):

        return 1
    
    else:

        return (n*factorial(n-1))

# Explaining to the user what factorial means, using an example.
print("\nThe factorial of a number is the product of all positive integers from 1 to that number, inclusive.\n\
For example:\n4! = 1*2*3*4 = 24 \n")

# Taking user input
n=int(input("\nPlease enter the number :- "))

# Displaying result
print(f"\nFactorial of {n} = {factorial(n)}\n")
