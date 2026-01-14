'''Q9:- Create a dictionary where the keys are the first 5 positive integers 
and the values are tuples containing the key and its square. Print the dictionary.'''

# Creating a dictionary where the keys are the first 5 positive integers 
# and the values are tuples containing the key and its square.
dict={i:(i,i**2) for i in range(1,6)}

# Displaying results
print(f"\nA dictionary where the keys are the first five positive integers, \
\nand the values are tuples containing each key and its square.")

print("\n",dict,"\n")