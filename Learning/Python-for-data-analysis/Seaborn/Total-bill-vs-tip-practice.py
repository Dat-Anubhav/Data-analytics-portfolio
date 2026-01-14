import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
tips

sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("Scatter plot of total bill vs tip")
plt.show()

'''Line plot'''

sns.lineplot(x='size',y='total_bill', data=tips)
plt.title("Line plot pof total bill by size")
plt.show()
tips

'''Heatmap'''
data = np.random.randint(1, 100, (10, 10)) # 10x10 data matrix
sns.heatmap(data)
plt.show()