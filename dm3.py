#building the dataset
import quandl
import pandas as pd

api_key = 'VtW6RPJSrNoimLEML1D3'

df = quandl.get("BCIP/_XYHB", authtoken=api_key)

print(df.head())

df.rename(columns={'Open':'Start_Open'},inplace=True)

print(df.head())

