'''Q11:- Define a function that takes a single integer as input and returns the integer squared, 
cubed, and raised to the power of four. Test the function with different inputs.'''

# Defining a function that takes a single integer as input and returns the integer squared, 
# cubed, and raised to the power of four.
def integer(a):

    return (f"\n{a} squared = {a*a}, {a} cubed = {a**3}, {a} to the power four = {a**4}")

# Taking user input 
a=int(input("\nPlease enter the number :- \n"))

# Displaying result
print(integer(a),"\n")

