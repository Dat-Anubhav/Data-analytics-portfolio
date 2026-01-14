'''Q2:- Print the first, middle, and last elements of the list created in exercise 1.'''

# Created empty list
l=[]

for i in range(1,21):

    l.append(i)

# Displaying the list of first 20 positive integers
print("\nList of first 20 positive integers is = ",l)

# Displaying the first, middle, and the last element of the list created
print(f"\n\nFirst element of the list is = {l[0]}\
\nMiddle element of the list is = {l[9]}\
\nLast element of the list is = {l[19]}\n")