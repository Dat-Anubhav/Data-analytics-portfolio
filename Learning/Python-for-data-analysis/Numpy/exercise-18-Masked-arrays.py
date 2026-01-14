'''Q18:- Create a masked array of shape (4, 4) with random integers and mask the elements greater than 10. 
Compute the sum of the unmasked elements.'''

import numpy as np
import numpy.ma as ma

aray=np.random.randint(1,20, size = (4,4))
masked_array=ma.masked_greater(aray,10)

print("\nOriginal array :- \n",aray)
print("\nMasked array :- \n",masked_array)

# Computing the sum of the unmasked elements.
# Traditional loop for sum will not work here, u have to use .sum()
masked_array_sum=masked_array.sum()

print("\nThe sum of the unmasked elements = ",masked_array_sum,"\n")

'''A masked array is a NumPy array that allows you to mark certain elements as invalid or missing, 
so those elements are ignored during calculations—helping you handle incomplete or faulty data safely'''