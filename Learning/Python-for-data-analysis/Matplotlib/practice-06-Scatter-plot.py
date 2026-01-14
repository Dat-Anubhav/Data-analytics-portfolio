'''Scatter plot'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

plt.scatter(x,y, color='red', marker='x')# u can not change the maker size
plt.title("Scatter-plot")
plt.grid(True)
plt.show