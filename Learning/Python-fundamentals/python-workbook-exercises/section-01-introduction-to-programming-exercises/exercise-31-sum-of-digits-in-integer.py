'''Q31:-Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.'''

# Asking user to input 4 digit integer
n=int(input("\n Please enter 4 digit integer :-  "))

# Converting entered integer to string to the number of digits it consists  
N=str(n)

# Finding the length of string which will give number of character i.e number of digits our entered integer has 
d=str.__len__(N)

# Displaying umber of digits entered integer has
print("\nnumber of digits are = ",d)

# Error handling: if user input more than 4 digit integer 
if(d>4):
    print("\nINVALID INPUT\n")

# proceeding to calculations 
elif(d<=4):
    
    s=n%10 # extracting the 1st digit
    print(s) # displaying 1st digit
    S=0
    S=S+s # adding 1st digit of integer
    
    k=n//10 # Remaining digits
    s=k%10 # extracting the 2nd digit 
    print(s) # displaying 2nd digit
    S=S+s # adding 2nd digit of integer
    
    k=k//10 # Remaining digits
    s=k%10 # extracting the 3rd digit
    print(s) # displaying 3rd digit
    S=S+s # adding 3rd digits of integer
    
    k=k//10 # Remaining digits
    s=k%10 # extracting the 4th digit
    print(s) # displaying 4th digit
    S=S+s # adding 4th digits of integer
    
    print("Sum of digits in integers = ",S)


