#!/usr/bin/env python
# coding: utf-8

# In[26]:


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


#M2 Money supply in billions
M2 = fred.get_series('WM2NS')

#M2 Series to dataframe
df_M2 = M2.to_frame().reset_index()
headers_M2 = ["Date","M2"]
df_M2.columns = headers_M2

#Line chart Matplolib - M2
df_M2.plot (kind='line', x='Date', y='M2', color = 'red', figsize = (10,6))
plt.title('M2 Money Supply')
plt.ylabel('M2 in Billion $')
plt.xlabel('Year')


#Mortgage rate average 30Y USA
MORTGAGE = fred.get_series('MORTGAGE30US')

#MortgageRate to dataframe
df_Mo = MORTGAGE.to_frame().reset_index()
headers_Mo = ["Date","Mortgage Rate"]
df_Mo.columns = headers_Mo

#Line chart Matplolib - Mortgage Rate
df_Mo.plot (kind='line', x='Date', y='Mortgage Rate', color = 'green', figsize = (10,6))
plt.title('Motgage Rate 30Y fixed')
plt.ylabel('Mortgage Rate in %')
plt.xlabel('Year')

# Core inflation
inflation = fred.get_series('CORESTICKM159SFRBATL')

#Core inlfation to dataframe
df_core = inflation.to_frame().reset_index()
headers_Mo = ["Date","Core inflation"]
df_core.columns = headers_Mo

#print(df_core.tail(20))

#Line chart Matplolib - Core inflation
df_core.plot (kind='line', x='Date', y='Core inflation', color = 'green', figsize = (10,6))
plt.title('Core Inflation')
plt.ylabel('Core inflation in %')
plt.xlabel('Year')

#S&P500 daily close
SP500 = fred.get_series('SP500')

#SP500 Series to dataframe
df_SP500 = SP500.to_frame().reset_index()
headers_SP500 = ["Date","SP500"]
df_SP500.columns = headers_SP500

#Line chart Matplolib - SP500
df_SP500.plot (kind='line', x='Date', y='SP500', color = 'red', figsize = (10,6))
plt.title('SP500 daily close')
plt.ylabel('SP500')
plt.xlabel('Year')



# In[ ]:





# In[ ]:




