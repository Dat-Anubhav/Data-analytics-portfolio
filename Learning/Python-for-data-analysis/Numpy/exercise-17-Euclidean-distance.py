'''Q17:-Create a structured array with fields 'x' and 'y' (both integers). 
Add some data and compute the Euclidean distance between each pair of points.'''

import numpy as np

data_type=[('X','i4'),('Y','i4')]

arr=np.array([(1,2),(3,4),(5,6)], dtype=data_type)

print("\nA structured array with fields 'x' and 'y' (both integers). \n")
print(arr)

# For two points(x1,y1)(x2,y2) in a 2D plane, the Euclidean distance = underoot((x2-x1)^2+(y2-y1)^2) 

# computing the Euclidean distance between each pair of points.
eu_dis=np.sqrt((arr['X'][:,np.newaxis]-arr['X'])**2+(arr['Y'][:,np.newaxis]-arr['Y'])**2)

print("\nThe Euclidean distance between each pair of points :-")
print(eu_dis)


'''Reading the Example Output
Given your points: 
[(1,2),(3,4),(5,6)], the matrix is:-

[[0.         2.82842712 5.65685425]
 [2.82842712 0.         2.82842712]
 [5.65685425 2.82842712 0.        ]]

The value 2.82842712 at row 0, column 1 is the distance between point 1 (1,2) and point 2 (3,4).

The value 5.65685425 at row 0, column 2 is the distance between point 1 (1,2) and point 3 (5,6).

The diagonal entries are always 0, since the distance from a point to itself is zero.

This matrix is symmetric: the distance from 

How to Use This Matrix:-
This format is essential for clustering (like K-means), nearest neighbor search, or understanding relationships between data points.

For any pair of points, you can directly look up the distance without recalculating.

Key Point
The resulting matrix provides a complete picture of how far apart all your points are from each other in Euclidean (straight-line) terms, all at once'''



'''Why Use np.newaxis Here?
Without np.newaxis, data['x'] and data['y'] are 1D arrays.

Adding np.newaxis transforms a 1D array of shape (n,) into a 2D array of shape (n, 1).

This reshaping makes it possible to subtract each x-coordinate (or y-coordinate) from every other x-coordinate (or y-coordinate) in a single operation. 
(like a matrix subtraction otherwise it will subtract one element at a time but by using newaxis each element is get subtracted in a single operation)
[,np.newaxis] for convert into column, [np.newaxis,:] for converting into row'''