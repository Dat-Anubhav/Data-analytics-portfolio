'''Create a NumPy array of shape (3, 3) with values from 1 to 9. Normalize the array (i.e., 
scale the values to have a mean of 0 and a standard deviation of 1).'''

import numpy as np

# Creating a NumPy array of shape (3, 3) with values from 1 to 9.
arr=np.random.randint(1,9, size=(3,3))

# Displaying the array to the user
print(f"\nThe array :-\n{arr}")

# Finding mean
mean=np.mean(arr)

# Finding standard deviation
std_dev=np.std(arr)

# Calculating the normalised array
normalised_array=(arr-mean)/std_dev

# Displaying results
print(f"\nMean = {round(mean,2)}\
\n\nStandard deviation = {round(std_dev,2)}\
\n\nNormalised array :- \n\n{normalised_array}\n")


'''
Purpose of Normalization
Normalization (specifically Z-score normalization here) adjusts the values so that:

The mean of the array becomes 0.

The standard deviation becomes 1.

This is done by subtracting the mean and dividing by the standard deviation for each element:

normalized value = (original value - mean)/standard deviation
 
Why Normalize the Array?
Standardization: Algorithms in data analysis and machine learning often work better when data is standardized. Features (or values) on the same scale 
allow models to converge faster and avoid bias caused by scale differences.

Interpretability: It makes different datasets comparable.

Mathematical Stability: Some mathematical operations (e.g., distance calculations, regression, neural networks) 
function more reliably when the data range is controlled.'''