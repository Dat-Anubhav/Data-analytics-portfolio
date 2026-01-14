'''Q8:- Write a program that calculates the factorial of a number input by the user using a while loop.'''

# Displaying the objective of this program to the user
print("\nThis program calculates the factorial of any input number")

# Taking user input
n=int(input("\nPlease input the number whose factorial has to be calculated = "))

i=1
f=1 # f holds the value of n!
while(i<=n):

    f=f*i
    i+=1

# Diplaying results
print(f"\nFactorial of {n} is = {f}")    

