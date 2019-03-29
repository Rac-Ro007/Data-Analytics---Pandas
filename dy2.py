#quandl.get("ZILLOW/C12427_ZHVISF", authtoken="VtW6RPJSrNoimLEML1D3")

import pandas as pd

# df = pd.read_csv('ZILLOW-C12427_ZHVISF.csv')

# print(df.head())

# df.set_index('Date',inplace=True)

# print(df.head())

# df.to_csv('newcsv.csv')

# df = pd.read_csv('newcsv.csv',index_col=0)

# print(df.head())

# df.columns=['Will_HFI']  #renames ALL COLUMNS TO ''

# print(df.head())

# df.to_csv('newcsv4.csv',header=False)

# print(df.head())
# df = pd.read_csv('newcsv4.csv',names=['Date','Aus_HFI'],index_col=0)

# print(df.head())

# df.to_html('exam.html')

df = pd.read_csv('newcsv4.csv',names=['Date','Val_HI'])

print(df.head())

df.rename(columns={'Val_HI':'7706_HI'},inplace=True)

print(df.head())
