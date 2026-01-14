'''Q6:- Define a function that takes two integers as input and returns their sum. 
Test the function with different inputs.'''

# Defining a function that takes two integers as input and returns their sum.
def integer_sum(a,b):

    return a+b
# Taking user input for the first integer
a=int(input("\nPlease enter the first integer : "))

# Taking user input for the second integer
b=int(input("\nPlease enter the second integer : "))

# Displaying the sum
print(f"\nSum of {a} & {b} = {integer_sum(a,b)}")