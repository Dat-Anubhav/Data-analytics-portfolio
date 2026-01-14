import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading the data from 'data.csv'
df=pd.read_csv('data.csv')

# Displaying the original dataframe
print("\nOriginal dataframe :- ")
print(df)

# Calculating mean of 'Value' column
value_mean=df['Value'].mean()
# Calculating mean of 'Sales' column
sales_mean=df['Sales'].mean()

# Displaying Value and Sales column mean
print("\nValue column mean = ",value_mean)
print("\nSales column mean = ",sales_mean)

# # Filling missing numeric values with column means
df.fillna(df.mean(numeric_only=True), inplace=True)

# Printing modified data after filling missing values
print("\nModified data :- ")
print(df)

# Plotting scatter plot for Category vs Value
plt.scatter(df['Category'],df['Value'], color='red', marker='x')
plt.show()

# Displaying which category has the highest value
print("\nCategory B has the highest value\n")

# Plotting bar chart for Product vs Sales
plt.bar(df['Product'],df['Sales'])
plt.show()

# Displaying which product has the highest sale
print("\nProduct 2 has the highest sale\n")
