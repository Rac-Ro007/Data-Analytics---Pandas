#Pickling
import quandl
import pandas as pd
import pickle

api_key = 'VtW6RPJSrNoimLEML1D3'

def get_initial_quan():
	abbr = ['YHB','HBB','HBD']
	main_df = pd.DataFrame()
	# for i in abbr:
	# 	query = "BCIP/_X"+str(i)
	df = quandl.get('BCIP/_XYHB', authtoken=api_key)


	if main_df.empty:
		main_df = df
	else:
		main_df = main_df.join(df)

	print(main_df.head())

	#storing from Pickle
	pic_out = open('demi_1.pickle','wb')
	pickle.dump(main_df,pic_out)
	pic_out.close()

get_initial_quan()

#Reading from Pickle
pic_in = open('demi_1.pickle','rb')
Fdata = pickle.load(pic_in)
print(Fdata)

#using pandas pickle
# from pandas import pickle
Fdata.to_pickle('pic.pickle')
Fdata2 = pd.read_pickle('pic.pickle')
print(Fdata2)



