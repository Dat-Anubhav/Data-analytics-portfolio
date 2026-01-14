'''Multiple plots'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.figure(figsize=(9, 5)) # Set the figure size: width=9, height=5

# Plot-1
plt.subplot(2,2,1)
plt.plot(x,y1, color='red')
plt.title("Plot-1")
plt.grid(True)
plt.show

# plot-2
plt.subplot(2,2,2)
plt.plot(y1,x, color='green', marker='o')
plt.title("Plot-2")
plt.show

# plot-3
plt.subplot(2,2,3)
plt.plot(x,y2, color='blue', marker='x')
plt.title("Plot-3")
plt.grid(True)
plt.show

# plot-4
plt.subplot(2,2,4)
plt.plot(y2,x, color='violet', marker='*', markersize=7)
plt.title("Plot-4")
plt.show
