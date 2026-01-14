'''Q10:- Write a program that checks if a number input by the user is a prime number using a for loop.'''

# Displaying the objective of this program to the user
print("\nThis program determines whether the number entered by the user is prime.")

# Taking user input
n=int(input("Please enter the number that has to be checked :- "))

prime = True

# Checking if n is less than or equal to 1, since numbers ≤ 1 are not prime
if(n<=1):

    prime = False

for i in range(2,n):

    if(n%i==0):

        prime=False
        break

# If the prime variable is True, the input number is prime
if(prime):

    print(f"\n{n} is a prime number")

else:

    print(f"\n{n} is not a prime number")












