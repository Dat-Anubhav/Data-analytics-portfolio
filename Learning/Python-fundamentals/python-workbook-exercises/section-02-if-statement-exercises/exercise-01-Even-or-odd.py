'''Q1:-Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.'''

"""
Summary :- This program checks whether an integer is even or odd
"""
# Displaying objective of this program
print("\nThis program checks whether an integer is even or odd\n")

# Taking user input
n=int(input("\nPlease enter the integer :- "))

# Checking entered integer is even or not
if(n%2==0):
    print(f"\nEntered integer {n} is even \n")
# Checking entered integer is odd or not
elif(n%2!=0):
    print(f"\nEntered integer {n} is odd \n")
# if user entered integer zero
else:
    print(f"\nEntered integer {n} is zero \n")
