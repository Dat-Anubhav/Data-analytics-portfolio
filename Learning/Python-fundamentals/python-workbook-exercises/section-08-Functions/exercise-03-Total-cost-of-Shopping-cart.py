'''Calculate the Total Cost Of Items In a Shopping Cart'''

# Defining the function to compute total shopping cart cost
def total_cost_of_shopping_cart(cart):
    
    total__cost=0
    
    # Loop through each item in the cart
    for items in cart:
        # Adding cost for current item (price * quantity) to total cost
        total__cost=total__cost+(items['price']*items['quantity'])

    # Returning the final total cost
    return total__cost

# List representing the shopping cart with item details
cart=[
{'name':'orange','price':45,'quantity':4},
{'name':'apple','price':60,'quantity':3},
{'name':'banana','price':20,'quantity':5}
]

# Displaying the cart to the user for reference
print("\nCart = ",cart,"\n")

# Printing the result of total cart cost
print("\nTotal cost of the shopping cart = ",total_cost_of_shopping_cart(cart),"\n")