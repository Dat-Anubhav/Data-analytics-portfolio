'''Q6:- Create a list of random numbers and sort it in ascending and descending order. 
Remove the duplicates from the list and print the modified list.'''

# Importing the random module for number generation
import random

# Generate a list of 15 random integers between 1 and 20
random_list=[random.randint(1,20) for _ in range(15)]

print("\nrandom list = ",random_list)

# Sorting the list in ascending order
ascending_list=sorted(random_list)

print("\nAscending list = ",ascending_list)

# Sorting the list in descending orde
descending_list=sorted(ascending_list,reverse=True)

print("\nDesecnding list = ",descending_list)

# Removing duplicates by converting the list to a set
remove_duplicates=set(random_list)

# Printing the final list with duplicates removed 
print("\nRemoving duplicates:- ")

print(f"\nFinal modified list is = {remove_duplicates}\n")

'''The underscore _ is used as a variable name in the for loop part of the list comprehension.
It's a common Python convention for situations where the variable itself is not needed—
only the number of iterations is important.

The underscore _ acts as a “throwaway” variable since you never actually use it inside the loop;
it just ensures the code runs 15 times.

Using _ is a handy way to indicate that the loop variable is intentionally unused 
and to make your code clearer to others.

You could also use a regular variable name, like i or num, instead of _; 
the code will work the same way if you don't need to reference the variable inside the loop.
'''
