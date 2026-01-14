'''Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.'''

"""
Summary:- This program calculates the amount in a savings account after 1, 2, and 3 years
i.e compound interest with an annual interest rate of 4%.
"""

# taking input from the user
amount=float((input("enter  your amount :- ")))

# interest rate
r=0.04

# OPTION 1:-
# doing it year by year 

amount1=amount*r+amount
# this is the amount you will recieve after 1 year

amount2=amount1*r+amount1
# this is the amount you willrecieve after 2 year

amount3=amount2*r+amount2
# this is the amount you will recieve after the third year

# final output
print(f"Your dposited amount is = {amount}\nAfter 1 year ayour amount will be with 4% of interest per year = {amount1}\n\
After 2 years your amount will be with interest rate as 4% per year will be = {amount2}\n\
After 3 years your amount will be with interest rate as 4% per year will be i.e final amount ={amount3} ")

# greeting message
print("THANKS FOR INVESTING WITH US")

# OPTION 2:-
# BY using the compound interest formula

''' formula for compound interest
 A = P (1 + r/n)^(nt)
 WHERE A is the amount of money accumulated after n years, including interest
 P is the principal amount (the initial amount of money)
 r is the anual interest rate (decimal)
 n is the number of times that interest is compunded per year
 t is the time the money is invested for in years'''

# here is n=1 and t=3 ,p= amount(user input) , r=0.04 ie 4% interest rate

# putting the values we get
A=amount*(1+r/1)**(1*3)

# by using this formula we can directly calculate the final amount after 3 years
print(f"the final amount after 3 years with 4% interest rate is = {A}")