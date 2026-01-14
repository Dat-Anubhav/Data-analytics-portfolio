'''Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.

A one dollar coin was introduced in Canada in 1987. It is referred to as a
loonie because one side of the coin has a loon (a type of bird) on it. The two
dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
derived from the combination of the number two and the name of the loonie.'''

"""
Summary
"""
# 1 cent = 1/100 dollar
# 1 loonie = 1 dollar = 100 cents
# 1 toonie = 2 dollar = 200 cents
# 1 pennies = 1 cent
# 1 nickels = 5 cents
# 1 dimes = 10 cents
# 1 quarters = 25 cents 

# taking the user input in cents
cent=int(input("\nEnter the amount that to be returned in cents :- "))

print("\nIn Canadian currency you have to give change in following coins :- \n")

can=cent
# holding the user input to calculate only canadian coins 
# so that we can display the result in canadian and in us coins


toonies = can//200
can= can%200

loonies = can//100

print("toonies = ",toonies)
print("loonies =",loonies)
print(f"\nTotal number of coins that need to be return the change = {int(toonies)+int(loonies)} coin\n")

# calculating the number of coins required to return the change
quarter=cent//25
change=cent%25
dimes=change//10
change=change%10
nickel=change//5
change=change%5
pennies=change//1

# displaying the result 
print("\nIn U.S currency you have to give change in following coins :- \n")
print("quarters= ",quarter)
print("dimes = ",dimes)
print("nickel = ",nickel)
print("pennies = ",pennies)

print(f"\nTotal number of coins that need to be return the change = \
{(quarter)+(dimes)+(nickel)+(pennies)} coin \n")

#Greeting the user 
print("THANKS FOR USING OUR SERVICE :)\nHAVE A NICE DAY AHEAD :)\n")