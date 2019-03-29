#Plotting and Percent change and correlation
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = 'VtW6RPJSrNoimLEML1D3'
# api_key = open('quandlapikey.txt','rb').read()

def get_initial_quan():
	abbr = ['YHB','HBB','HBD']
	main_df = pd.DataFrame()
	# for i in abbr:
	# 	query = "BCIP/_X"+str(i)
	df = quandl.get('BCIP/_XYHB', authtoken=api_key)
	# df = df.pct_change() #---> stored in demi_1f.pickle
	df['Open'] = (df['Open'] - df['Open'][0]) / df['Open'][0] * 100.0   #Percent change

	if main_df.empty:
		main_df = df
	else:
		main_df = main_df.join(df)

	print(main_df.head())

	#storing from Pickle
	pic_out = open('dem3.pickle','wb')
	pickle.dump(main_df,pic_out)
	pic_out.close()

def HPI_Bench():
	df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
	# df['United States'] = (df['United States'] - df['United States'][0]) / df['United States'][0] * 100.0  
	df['NSA Value'] = (df['NSA Value'] - df['NSA Value'][0]) / df['NSA Value'][0] * 100.0  
	return df

# get_initial_quan()
# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))

Fdata = pd.read_pickle('dem3.pickle')
bench = HPI_Bench()
# Fdata['Close'] = Fdata['Close'] * 2
# print(Fdata['Close'])
# Fdata.plot(ax=ax1)
# bench.plot(ax=ax1,color='k',linewidth=10)
# plt.legend().remove()
# plt.show()

#COrrelation
Fdata_Cor = Fdata.corr()
print(Fdata_Cor.head)
print(Fdata_Cor.describe())

