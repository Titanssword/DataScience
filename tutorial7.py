# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:38:44 2016

@author: CJ
"""
"""
using "pip install quandl " to install quandl modules
"""
import quandl
import pandas as pd
import html5lib
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
"""
get the dataframe from the quandl by using the authtoken
"""

df = quandl.get("SWA/1B", authtoken="FJF42_NFf8551EUVpR3W")

print(df.head())
pickle_out = open('fiddy_states.pickle','wb')
pickle.dump(df, pickle_out)
pickle_out.close()        

HPI_data = pd.read_pickle('fiddy_states.pickle')

HPI_data['Home Price Index2'] = HPI_data['Home Price Index']*2

print(HPI_data[['Home Price Index2','Home Price Index']].head())
print(HPI_data)
fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
HPI_data.plot(ax=ax1,color='b',linewidth=1)
plt.legend().remove()
plt.show()
HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)
print(HPI_State_Correlation.describe())