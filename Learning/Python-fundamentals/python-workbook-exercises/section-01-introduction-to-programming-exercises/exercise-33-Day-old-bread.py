'''Q33:-A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.'''

l=int(input("enter the loaves of day old bread:- "))

sp=3.49 # bakery sells loaves of bread for $3.49 each
tot=sp*l
print(f"\nOur bakery sells loaves of bread for $3.49 each")
print(f"\nRegular price of the bread is = {round(tot,2)} $")
print(f"\n60% discount on day old bread = {round(tot*60/100,2)}")
print(f"\ntotal price that to be paid = {round(tot-(tot*60/100))}")

# Greeting message
print("\nTHANKS FOR PURCHASING \nPLEASE VISIT AGAIN :)\n")