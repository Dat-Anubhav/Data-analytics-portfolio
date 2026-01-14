'''Q3:- Print the first five elements, the last five elements,
 and the elements from index 5 to 15 of the list created in Assignment 1.'''

'''METHOD 1:- # using for loop
# Created an empty list
l=[]

for i in range(1,21):

    l.append(i)

# Displaying the list of first 20 positive integers
print("\nList of first 20 positive integers is = ",l)

# Displaying first five elements of the list created
print(f"\nFirst five elements of the list created are :- ")
for i in range(5):

    print(l[i])

# Displaying last five elements of the list created
print(f"\nLast five elements of the list created are :- ")
for j in range(14,20):

    print(l[j])

# Displaying elements from index 5 to 15 of the list created
print(f"\nElements from index 5 to 15 of the list created are :-")

for k in range(4,15):

    print(l[k])'''

'''METHOD 2:- # By slicing list '''

# Created an empty list
l=[]

for i in range(1,21):

    l.append(i)

# Displaying the list of first 20 positive integers
print("\nList of first 20 positive integers is = ",l)

# Displaying first five elements of the list created
print(f"\nFirst five elements of the list created are :- {l[:5]}")

# Displaying last five elements of the list created
print(f"\nLast five elements of the list created are :- {l[14:20]}")

# Displaying elements from index 5 to 15 of the list created
print(f"\nElements from index 5 to 15 of the list created are :- {l[4:15]}\n")