'''Q23:- A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.

Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.'''

# Displaying the objective of this program to user
print("\nThis program calculates and displays a detailed monthly cell phone bill \n\
based on usage minutes, text messages, additional charges, and taxes.\n")

# preventing the program from crashing: what if user input in string
try:
    # Taking user input for air time
    at=float(input("\nPlease enter the total air time used by the user :- "))
    # Taking user input for text messages
    tm=float(input("\nPlease enter the total text messages send by the user :- "))
except ValueError:
    print("\nINVALID INPUT: Please enter the information in correct format\n")
    exit()

# Checking conditions for base plan
if((at>=0 and at<=50) and (tm>=0 and tm<=50)):

    a=(15+0.44)+((15+0.44)*5/100)

    print(f"\nYour cell phone bill:- \n\n\
base amount = $15.00\n\
Support to 911 call centres = $0.44\n\
5% Sales tax = ${round(((15+0.44)*5/100),2)}\n\n\
Total amount = ${round(a,2)}\n")

# Checking conditions for additional services used
elif(at>50 or tm>50):

    additional_air_time=at-50
    additional_text_messages=tm-50
    # Additional air time cost
    ad_air_cost=additional_air_time*0.25
    # Additional text messages cost
    ad_text_cost=additional_text_messages*0.15

# Calculating the total bill amount including base plan, additional services, 911 support, and taxes
    Total_amount=(15+ad_air_cost+ad_text_cost+0.44)+((15+ad_air_cost+ad_text_cost+0.44)*5/100)
    
    # Generating the bill
    print(f"\nYour cell phone bill:- \n\n\
base amount = $15.00\n\
Each additional minute of air time costs $0.25\n\
Each additional text messages cost $0.15\n\
Additional air time used ={additional_air_time}\n\
Additional text messages send = {additional_text_messages}\n\
Additional air time cost = ${ad_air_cost}\n\
Additional text messages cost = ${ad_text_cost}\n\
Support to 911 call centres = $0.44\n\
5% Sales tax = ${round(((15+ad_air_cost+ad_text_cost+0.44)*5/100),2)}\n\n\
Total amount = ${round(Total_amount,2)}\n")

# ERROR HANDLING: for negative input
else:
    print("\nINVALID INPUT\n")

print("\nWe appreciate your business. Stay connected!\n")