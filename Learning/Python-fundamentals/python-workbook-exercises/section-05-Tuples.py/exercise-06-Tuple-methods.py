'''Q6:- Create a tuple with duplicate elements and count the occurrences of an element. 
Find the index of the first occurrence of an element in the tuple.'''

t=(1,2,2,"hello",4,6,2,7,44)

# Displaying the tuple created above
print(f"\nTuple with duplicate elements is = {t}\n")

# Counting and displaying the number of occurrences of the element 2 in the tuple.
print("\nNumber of 2's are = ",t.count(2))

# Displaying the index of the first occurrence of element 2
print(f"\nIndex of the first occurrence of element 2 = {t.index(2)}\n")