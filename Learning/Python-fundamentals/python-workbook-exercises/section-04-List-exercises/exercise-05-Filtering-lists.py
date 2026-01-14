'''Q5:- Create a new list containing only the even numbers from the list created in Assignment 1 
using a list comprehension. Print the new list.'''

# List created in previous exercise
lis=[i**2 for i in range(1,11)]

print(f"\nFirst 10 squares list = {lis}")

even_list = [j for j in lis if j%2==0]

# Displaying only even numbers from the list
print(f"\nEven numbers in the list = {even_list}\n")
