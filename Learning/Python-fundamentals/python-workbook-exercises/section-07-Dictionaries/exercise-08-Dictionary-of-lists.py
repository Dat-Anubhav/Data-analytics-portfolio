'''Q8:- Create a dictionary where the keys are the first 5 positive integers 
and the values are lists containing the first 5 multiples of the key. Print the dictionary.'''

# Creating a dictionary where each key are the first 5 positive integers 
# and the values are lists containing the first 5 multiples of the key, 
# using dictionary comprehension
dictionary_of_list={i:[i*j for j in range(1,6)] for i in range(1,6)}


# Displaying results
print(f"\nA dictionary where each key is one of the first five positive integers, \
and each value is a list containing \nthe first five multiples of that key, \
created using dictionary comprehension\n")

print(dictionary_of_list,"\n")
