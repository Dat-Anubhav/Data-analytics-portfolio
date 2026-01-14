'''Pie-chart'''

import matplotlib.pyplot as plt

labels=['A','B','C','D']
sizes=[30,20,40,10]
colors=['gold','lightgreen','coral','skyblue']
explode=(0.1,0,0,0) # moving out the 1st slice i.e A slice

# Creating a pie-chart
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True)
plt.title("Pie-chart")
plt.show