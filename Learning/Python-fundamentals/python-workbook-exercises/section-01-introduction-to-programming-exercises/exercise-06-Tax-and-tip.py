'''Q6:- The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.'''

#Summary:- this program is to calculate the tax ,tip and total cost of a meal in a restaurant. 

# Get the cost of the meal from the user
Cost=float(input("enter the cost of the meal :- "))

#Tax in india on meal in most of the restaurant is 5% 
Tax=5/100*Cost

# Tip is 18% od the meal amount
Tip=18/100*Cost

# Total cost paid by the user in a restaurant for a one time meal 
# is total cost= meal amount+tax+tip
Total_cost=Cost+Tax+Tip

# Formatting the output so that all of the values are displayed using two decimal places 
print(f"\nCost of the one time meal in a restaurant :- {Cost}\
      \n Tax is 5% on a meal in a Indian restaurant\
      \n Tax amount is :- {Tax}\
      \n Tip is 18% on a meal in a Indian restaurant\
      \n tip amount is :- {Tip}\
      \n\
      \n Total amount paid by the user including of tax and tip is :- {Total_cost}"
      )
# \n is used to print in next line
# \ is used to break the line of code
# f is used for formatted string literals

# Displaying a greating mnessage on the bill
print("\n\'THANKS FOR DINNING PLEASE VISIT AGAIN\'")
