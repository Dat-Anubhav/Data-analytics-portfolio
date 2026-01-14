'''Q9:- Write a program that calculates the sum of the digits of a number input by the user using a while loop.'''

# Displaying the objective of this program to the user 
print("\nThis program calculates the sum of digits of a number")

# Taking user input
n=int(input("\nPlease enter the number whose sum of digits has to be calulated = "))

# Calculating the number of digits present in the input number 
len=str.__len__(str(n))

print(f"\nNumber of digits present in {n} = ", len)

i=0
s=0
while(i<len):

   k=n%10 # Extracting the first digit
   print(k) # printing each extracted digit
   s=s+k # calculating the sum of digits
   n=n//10 # Storing the rest of the digits
   i+=1

# Displaying result 
print(f"Sum of digits = {s}") 

