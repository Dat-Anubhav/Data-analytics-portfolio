'''An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.'''

"""Summary:- This program calculates the total weight of an order based on the number of widgets and gizmos.
"""
# taking input from user
w=int(input("enter the number of widgets :- "))
g=int(input("enter the number of gizmos :- "))

# weight of weights and gizmos are 75 grams and 112 grams respectively

# formula for total weight
total_weight= w*75+g*112

 
print(f"wedget weight:-75 g each \ngizmos weight :- 112 g each\n \
total weight for {w} wedgets and {g} gizmos is = {total_weight} grams")
