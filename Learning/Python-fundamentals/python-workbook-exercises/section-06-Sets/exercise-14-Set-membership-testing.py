'''Q14:- Create a set and test if certain elements are present in the set. Print the results.'''

# Creating a set of first 10 positive integers
s={i for i in range(1,11)}

# Displaying the set to the user for reference
print(f"\nThe set is = {s}\n")

# Testing whether 6, 5, and 12 are present in the set and displaying the results.
print("6 present in the set = ",6 in s)
print("5 present in the set = ",5 in s)
print("12 present in the set = ",12 in s)