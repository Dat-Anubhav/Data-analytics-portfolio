'''Q4:- Write a program that asks the user to input numbers until they input 0.
The program should print the sum of all the input numbers.'''

print("\nThis program print the sum of all the input integers\n")

# The variable "sum" will store the total of all the sums of the input numbers.
sum = 0

while True:

    print("\nPlease press 0 if u no longer want to input numbers\n")

    k=int(input("\nplease input the number = "))

    sum=sum+k
    print("\nSum of the all the input numbers is = ",sum)

    if(k==0):

        break
#  Greeting message
print("\nThanks for using integer sum calculator\n")
