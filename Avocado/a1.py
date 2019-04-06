import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

df = pd.read_csv('Datasets/avocado.csv')
print(df.head())

df.set_index('Date',inplace=True)
print(df.head())

# df.to_csv('Datasets/ind_date_avocado.csv')
#printing avg column
print(df['AveragePrice'].tail())

#extracting dataframe of region 'Albany'
alb_df = df[df['region']=='Albany']
print(alb_df.tail())

#plotting the average value
fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
alb_df['AveragePrice'].plot(ax=ax1)
plt.show()