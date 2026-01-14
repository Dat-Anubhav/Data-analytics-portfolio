'''Q7:- Define a function that takes two integers as input and returns their sum. 
The second integer should have a default value of 5. Test the function with different inputs.'''

# Defining a function that takes two integers as input and returns their sum. 
# The second integer has a default value of 5.
def integer_sum(a,b=5):

    return a+b

# Displaying result
print(f"\nThe Sum is = {integer_sum(5,7)}")