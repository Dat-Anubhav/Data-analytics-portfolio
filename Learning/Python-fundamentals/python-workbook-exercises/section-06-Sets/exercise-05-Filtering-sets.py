'''Q5:- Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. 
Print the new set.'''

# Creating a new set containing the squares of the first 10 positive integers using a set comprehension.
s=set(i**2 for i in range(1,11))

# Displaying set to the user for reference
print(f"\nThe set containing the squares of the first 10 positive integers = {s}\n")

# Creating a new set containing only the even numbers from the set created above.
even_set=set(e for e in s if(e%2==0))

# Displaying set containg only even numbers
print(f"\nThe new set containing only the even numbers = {even_set}\n")
