'''Q12:- Create a set and remove elements from it until it is empty. Print the set after each removal.'''

# Creating a set
s={i for i in range(1,11)}

# Finding the length of the set to use as the loop condition. 
length=len(s)

# Displaying the set to the user for reference 
print(f"The set is = {s}\n")

j=1 # initialisation for while loop

# Displaying the set after every removal
print("removing elements one by one:- \n")
while (j<=length):
    
    s.remove(j)
    print(s)
    j+=1