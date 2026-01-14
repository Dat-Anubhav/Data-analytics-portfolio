'''Q19:- Create a masked array of shape (3, 3) with random integers and mask the diagonal elements. 
Replace the masked elements with the mean of the unmasked elements.'''

import numpy as np
import numpy.ma as ma

aray=np.random.randint(1,20, size=(3,3))
masked_aray=ma.masked_array(aray, mask=np.eye(3,dtype=bool)) # It masks (hides) all diagonal elements 
# of the 3x3 array for further operations.

print("\nOriginal array = \n",aray)
print("\nMasked_array = \n",masked_aray)

# Cslculating the mean of the unmasked elements.
mean=masked_aray.mean()
print("\nMean of unmasked elements = ",mean)

# Replacing the masked elements with the mean of the unmasked elements.
fill_mean=masked_aray.filled(mean)

print("\nModified masked array :- \n")
print(fill_mean)