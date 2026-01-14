'''Q5 :- In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.''' 

#taking the user input that how many containers he/she has of
# 1 litre or less than litre or more than 1 litre

con1=int(input("enter the number of container of size 1 litre or less than 1 litre :-"))
con2=int(input("enter the number of containers of seize greater than 1 litre :- "))

#doing calculation 
# multiplying the number of containers with the deposit amount to get the refund value

refund=con1*0.10 + con2*0.25

#Displaying the result to the user

print(f"your total refund amount for {con1} (1 or less than 1 litre drink containers) \nand \
{con2} (more than a litre drink containers)\n ie {con1+con2} drink containers is = ${float(refund)}")

#used float type conversion to display the refund value in in decimals
# # here i have made f string to print the result in the formated way
# also used \ to type in the next line because print statement is too long
# and used \n to print the results in a new line in the output 

print("Thanks for recycling")
# Greeting the user for recycling
