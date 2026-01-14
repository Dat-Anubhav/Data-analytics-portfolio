'''Q10:- Define a function that contains another function inside it. 
The outer function should take two integers as input and return the result of the inner function, 
which multiplies the two integers. Test the function with different inputs.'''

# Defining the outer function which is taking two integer arguments
def outer_function(x,y):

    # Defining the inner function for multiplying two input values
    def inner_function(a,b):

        return a*b
    
    # Calling the inner function with outer function's arguments and returning the result
    return inner_function(x,y)

# Testing and displaying result for outer_function with example value
print(f"\nProduct: {outer_function(2, 5)}\n")