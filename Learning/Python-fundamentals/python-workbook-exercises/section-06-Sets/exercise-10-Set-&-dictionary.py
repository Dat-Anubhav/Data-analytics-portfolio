'''Q10:- Create a dictionary with set keys and integer values. Print the dictionary.'''

# As we know dictionary keys must be immutable, therefore we have to use frozenset here
dic={
frozenset({"ONE","one"}): 1,
frozenset({"TWO","two"}): 2,
frozenset({"THREE","three"}): 3,
frozenset({"FOUR","four"}): 4,
frozenset({"FIVE","five"}): 5
}

# Displaying results
print("\nA dictionary with set keys and integer values will look like :- \n")

print(f"\n{dic}\n")