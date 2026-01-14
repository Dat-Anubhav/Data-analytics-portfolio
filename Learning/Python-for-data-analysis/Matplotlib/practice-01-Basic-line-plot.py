'''Basic line plot'''

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=['a','b','c','d','e','f','g','h','i']

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic line plot")
plt.show