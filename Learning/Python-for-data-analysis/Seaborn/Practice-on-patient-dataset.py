import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your patient dataset
df = pd.read_csv('patients.csv')

# Displaying the patients dataset
print("\nPatients datasets :- \n\n",df)

# Create a pairplot using age and satisfaction, colored by service type
sns.pairplot(df, vars=['age', 'satisfaction'], hue='service')
plt.show()

# Displaying analysis
print("\nAnalysis :- ")
print("\nGeneral_medicine followed by ICU service is the most used service by the old age patients.")
print("\nThe emergency service has the highest satisfaction.")
print("\nThe ICU service has the least satisfaction and needs improvement.\n")

# Creating age groups for visualization (example: bins of 10 years)
df['age_group']=pd.cut(df['age'], bins=[0,20,40,60,80,100], labels=['0-20','21-40','41-60','61-80','81-100'])

pivot=df.pivot_table(index='service', columns='age_group', values='satisfaction')

# Drawing the heat map
sns.heatmap(pivot,annot=True, cmap='coolwarm')
plt.title("Average Satisfaction by Service and Age Group")
plt.show()

# Displaying analysis
print("\nAge group wise analysis :- ")
print("\nICU service has the highest satisfaction rate among the 0-20 age group\nbut needs improvement for the older age groups")
print("\nEMERGENCY service has the highest satisfaction rate among the 40-60 age group \nbut there is an urgent need of improvement for (61-80) age group")
print("\nGENERAL MEDICINE has the lowest satisfaction rate among the (61-80) age group and needs urgent improvement")
print("\nSURGERY has over all good satisfaction rate among all the age group but needs improvement for the (81-100) age group people\n ")
print("\nFROM ABOVE ANALYSIS WE CAN CONCLUDE, SERVICES FOR (60-80) AGE GROUP NEEDS TO BE IMPROVED\n")