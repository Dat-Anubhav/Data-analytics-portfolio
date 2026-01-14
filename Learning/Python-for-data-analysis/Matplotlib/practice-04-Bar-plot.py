'''Bar plot'''

import matplotlib.pyplot as plt

categories=['A','B','C','D','E']
values=[5,7,3,8,6]

plt.bar(categories,values, color='violet', edgecolor='black')
plt.title("Bar-plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show