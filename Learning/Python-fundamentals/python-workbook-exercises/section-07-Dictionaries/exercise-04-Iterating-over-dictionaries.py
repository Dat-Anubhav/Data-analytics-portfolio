'''Q4:- Iterate over the dictionary created in Assignment 1 and print each key-value pair.'''

# Recreating the dictionary of exercise 1
dict={i:i**2 for i in range(1,11)}

# Displaying the dictionary to the user for reference 
print("\nThe dictionary is = ",dict)

# .items() returns all key-value pairs in the dictionary
for i ,j in dict.items():

# Displaying items
    print(f"{i} : {j}") # i is the key and j is the value for each dictionary item