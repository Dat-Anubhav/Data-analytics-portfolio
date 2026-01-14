'''Q5:- Define a function that takes a single integer as input and returns its square. 
Test the function with different inputs.'''

# Defining a function that takes a single integer as input and returns its square. 
def integer_square(num):

    return num*num

# Taking user input
num=int(input("\nPlease enter the integer :-  "))

# Displaying results
print(f"Square of {num} is = {integer_square(num)}\n")