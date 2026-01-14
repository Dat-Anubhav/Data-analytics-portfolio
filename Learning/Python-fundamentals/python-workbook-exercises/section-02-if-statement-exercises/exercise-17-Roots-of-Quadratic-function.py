'''Q17:-A univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
c are constants, and a is non-zero. The roots of a quadratic function can be found
by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
the quadratic formula, shown below:

root =(−b ± √b2 − 4ac)/2a

The portion of the expression under the square root sign is called the discriminant.
If the discriminant is negative then the quadratic equation does not have any real roots.
If the discriminant is 0, then the equation has one real root. Otherwise the equation
has two real roots, and the expression must be evaluated twice, once using a plus
sign, and once using a minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function. Your program
should begin by prompting the user for the values of a, b and c. Then it should display
a message indicating the number of real roots, along with the values of the real roots
(if any).'''

# Displaying the objective of this program
print("\nThis program finds the root of a quadratic finction\n")

# Telling user about the quadratic function and roots
print("\nA univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and \n\
c are constants, and a is non-zero. The roots of a quadratic function can be found \n\
by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A \n\
quadratic function may have 0, 1 or 2 real roots.\n")

# asking user to input the values of a,b and c
print("\nPlease enter the values of a, b and  c to find the roots of the quadratic functions :- \n")
try:

    # Taking user input for a,b and c
    a=float(input("\nPlease enter the value of  'a' in the function ="))
    b=float(input("\nPlease enter the value of  'b' in the function ="))
    c=float(input("\nPlease enter the value of  'c' in the function ="))
except ValueError:
    print("INVALID INPUT")
    exit()

# checking condition for a (a must not be a zero in a quadrsatic function) 
if(a==0):
    print(f"\na i.e ({a}) cannot be zero in a quadratic function. By definition, \n\
a quadratic function must be a second-degree polynomial, \n\
meaning the highest exponent of the variable is 2.\n")
    exit()

# Importing math module to calculate the √b2 − 4ac i.e discriminant. 
import math

dis=(b**2)-(4*a*c)

if(dis<0):
    print(f"\nas discriminant {dis} is negative \n\
it means the quadratic equation does not have any real roots.\n")

elif(dis==0):
    print(f"\nas discriminant {dis} is zero \n\
it means the quadratic equation has only one real root.\n")
    root=-b/(2*a)
# Displaying roots value upto 3 decimal places    
    print(f"\nThat one root is = {round(root,3)}\n")

else:
    print(f"\nas discriminant {dis} is greater than zero \n\
it means the quadratic equation has two real roots\n")
    
    root1=(-b+(math.sqrt(dis)))/(2*a)

    root2=(-b-(math.sqrt(dis)))/(2*a)
# Displaying roots value upto 3 decimal places
    print(f"\nThe roots are = {round(root1,3)} and {round(root2,3)}\n")

# Displaying program completion message
print("Quadratic equation solved successfully.")