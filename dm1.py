import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
			 'Visitors':[25,67,82,34,56,76],
			 'Bounce_rate':[54,34,56,72,12,46]}

df = pd.DataFrame(web_stats)

print(df)

df = df.set_index('Day') #Returns a new data frame stored in df again 

# df.set_index('Day',inplace=True) -----For returning say data frame with the newly set index

print(df['Visitors']) # u can also Use it through '.'

print(df[['Visitors','Bounce_rate']])

print(df.Visitors.tolist())		# to output a list of that column 

print(np.array(df[['Visitors','Bounce_rate']]))   #since tolist() wont work for multiple's column numpy can be used

df2 = pd.DataFrame(np.array(df[['Visitors','Bounce_rate']]))

print(df2)