import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as numpy
style.use('fivethirtyeight')

df = pd.read_csv('Datasets/avocado.csv')
print(df.head())

df['Date'] = pd.to_datetime(df['Date'])

#extracting dataframe of region 'Albany'
alb_df = df.copy()[df['region']=='Albany']
alb_df.set_index('Date',inplace=True)

alb_df.sort_index(inplace=True)
print(alb_df.tail())

#array- values ------ list - tolist()
# print(df['region'].values.tolist())

#unique names only
# print(df['region'].unique())

graph_df = pd.DataFrame()

#remember we divided the main df with region=='albany' ... similarly we can divide with type like organic and use same flow
for region in df['region'].unique()[:16]:
    print(region)
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets!
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

print(graph_df.tail())

# #plotting the average value
fig = plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))
# #rolling to remove wild peaks
# alb_df['prices25ma'] = alb_df['AveragePrice'].rolling(25).mean()
# print(alb_df.tail())
# alb_df['prices25ma'].plot()
graph_df.plot()
plt.show()
