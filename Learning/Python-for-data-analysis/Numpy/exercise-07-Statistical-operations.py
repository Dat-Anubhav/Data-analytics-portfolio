'''Q7:- Create a NumPy array of shape (5, 5) filled with random integers. 
Compute the mean, median, standard deviation, and variance of the array.'''

import numpy as np

# Creating an NumPy array of shape (5, 5) filled with random integers.
arr=np.random.randint(1,20, size=(5,5))

# Displaying the original array to the user
print(f"\nOriginal array :- \n\n{arr}")

# Computing the mean, median, standard deviation, and variance of the array.
mean=np.mean(arr)
median=np.median(arr)
standard_deviation=np.std(arr)
variance=np.var(arr)

# Displaying results
print(f"\nMean = {round(mean,2)}\
\nMedian = {round(median,2)}\
\nStandard deviation = {round(standard_deviation,2)}\
\nVariance = {round(variance,2)}\n")

'''
Standard deviation:- it is a practical, easy-to-interpret number that tells you the 
average distance a data point falls from the mean.

Variance:- it is a mathematical concept that calculates the average squared distance from the mean, 
making it less intuitive but useful for statistical theory.

'''
