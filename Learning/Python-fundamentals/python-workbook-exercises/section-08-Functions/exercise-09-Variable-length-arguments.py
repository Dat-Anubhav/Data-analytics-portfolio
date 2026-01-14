'''Q9:- Define a function that takes a variable number of integer arguments and returns their product. 
Test the function with different inputs.'''

# Defining a function that takes a variable number of integer arguments and returns their product.
def product(*args):

    pro=1
    # Iterating through each argument and multiplying it to the product
    for i in args:

        pro=pro*i

    return pro

# Displaying result
print(f"\nProduct = {product(2,5,6,3,6)}\n")