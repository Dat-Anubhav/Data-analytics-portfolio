'''Q13:- Create a nested tuple and iterate over the elements, printing each element.'''

# Creating nested tuple
tup=((1,2,3),(4,5,6),(7,8,9))

# Displaying the tuple to the user for reference
print(f"\nTuple is = {tup}\n")

# Iterating over each inner tuple in the outer tuple
for i in tup:
# Priting current inner tuple
    print(i)
    print("Its sub elements are :- ")
    
    for j in i:
#printing inner tuple sub-elements   
        print(j)