'''Histogram'''

import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.figure(figsize=(9,5))

# Plot-1
plt.subplot(1,2,1)
plt.hist(data,color='purple', edgecolor='black')
plt.title("Histogram")
plt.show

# plot-2
plt.subplot(1,2,2)
plt.hist(data,bins=3, color='magenta', edgecolor='black')
plt.title("Histogram with fix bins")
plt.show