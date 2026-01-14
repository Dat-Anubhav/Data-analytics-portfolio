import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")

total_sales=df.groupby('Product')['Sales'].sum()

# total_sales.plot(kind='bar', color='blue')

product_rgion=df.groupby('Product')['Region'].count()

print("\nProduct region wise;- \n",product_rgion)

product_rgion.plot(kind='bar', color='green')
