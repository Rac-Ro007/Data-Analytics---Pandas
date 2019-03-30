#Clubed of 1 to 8 Upto Correlation
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = 'VtW6RPJSrNoimLEML1D3'

# df = quandl.get("FMAC/HPI_AK", authtoken=api_key)

def states_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	# #this is a list
	# print(fiddy_states)
	#this is a dataframe
	# print(fiddy_states[0])
	#this is a column
	return fiddy_states[0][1][2:]

# df.rename(columns,inplace=True)
def get_inital_states_data():
	
	states=states_list()
	main_df = pd.DataFrame()
	
	for abbv in states:
		query="FMAC/HPI_"+str(abbv)
		
		df = quandl.get(query, authtoken=api_key)
		# df = df.pct_change() 
		df['NSA Value'] = (df['NSA Value'] - df['NSA Value'][0]) / df['NSA Value'][0] * 100.0   #Percent change

		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df,lsuffix='_left',rsuffix='_right')

		print(main_df.head())

		pickle_out = open('states3.pickle','wb')
		
		pickle.dump(main_df,pickle_out)
		
		pickle_out.close()

def HPI_Bench():
	df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
	# df['United States'] = (df['United States'] - df['United States'][0]) / df['United States'][0] * 100.0  
	
	df['NSA Value'] = (df['NSA Value'] - df['NSA Value'][0]) / df['NSA Value'][0] * 100.0   #Percent Change
	
	return df
# print(df.head())
# get_inital_states_data()   #Prepared DataSet(of Housing Price of all States in US) and Pickled it in states.pickle
# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))

HPI_Data = pd.read_pickle('states3.pickle')
# benchm=HPI_Bench()

# # print(HPI_Data)
# HPI_Data.plot(ax=ax1)
# benchm.plot(ax=ax1,color='k',linewidth=10)

# plt.legend().remove()
# plt.show()

#correlation
HPI_corr = HPI_Data.corr()
print(HPI_corr.head())

print(HPI_corr.describe())
