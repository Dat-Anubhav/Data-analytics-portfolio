'''Q16:- Create a structured array with fields 'name' (string), 'age' (integer), and 'weight' (float). 
Add some data and sort the array by age.'''

import numpy as np

data_type = [('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]
# defines three fields: name as a string of max 10 characters, age as 4-byte integer, 
# and weight as 4-byte float.

data = np.array([('Anubhav', 25, 55.5), ('Rishu', 30, 85.3), ('Rishi', 20, 65.2)], dtype=data_type)
print("\nOriginal array :- \n")
print(data)

# Sorting the array by age
sorted_data = np.sort(data, order='age')

# Displaying the sorted array
print("\nSorted array by age :- \n")
print(sorted_data,"\n")