'''Q11:- Write a program that prints the first n Fibonacci numbers, where n is input by the user.'''

# # Displaying the objective of this program to the user
print("\nThis program prints the first n fibonacci numbers")

# Taking user input
n = int(input("\nPlease Enter the number of Fibonacci numbers to print :- "))

a=0
b=1
count = 0
while count < n:
    print(a)
    k = a # k stores the previous value of a 
    a=b # a is updated to the previous value of b
    b = a + k # b is updated to the sum of the previous a and previous b
    count += 1

