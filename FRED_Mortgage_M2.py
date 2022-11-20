# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!pip  install fredapi
from fredapi import Fred 
import pandas as pd
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
fred = Fred(api_key='09488f1d12e3eabee7b6669b2d09db9a')

#Mortgage rate average 30Y USA
MORTGAGE = fred.get_series('MORTGAGE30US')


#M2 Money supply in billions
M2 = fred.get_series('WM2NS')


#S&P500 daily close
SP500 = fred.get_series('SP500')


#M2 Series to dataframe
df_M2 = M2.to_frame().reset_index()
headers_M2 = ["Date","M2"]
df_M2.columns = headers_M2

#M2
#Line Chart in Pandas
df_M2.plot.line(x='Date', y='M2')

#Line chart Matplolib
df_M2.plot (kind='line', x='Date', y='M2', color = 'red', figsize = (10,6))
plt.title('M2 Money Supply')
plt.ylabel('M2 in Billion $')
plt.xlabel('Year')


#MortgageRate
df_Mo = MORTGAGE.to_frame().reset_index()
headers_Mo = ["Date","Mortgage Rate"]
df_Mo.columns = headers_Mo
print(df_Mo)

#Line chart Matplolib
df_Mo.plot (kind='line', x='Date', y='Mortgage Rate', color = 'green', figsize = (10,6))
plt.title('Motgage Rate 30Y fixed')
plt.ylabel('Mortgage Rate in %')
plt.xlabel('Year')

print(MORTGAGE.tail(20))
