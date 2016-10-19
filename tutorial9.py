# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:43:56 2016

@author: CJ
"""

import quandl
import pandas as pd
import html5lib
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

HPI_data = pd.read_pickle('fiddy_states.pickle')
print("hello")
#print(HPI_data)

HPI_State_Correlation = HPI_data.corr()
#print(HPI_State_Correlation)
#print(HPI_State_Correlation.describe())

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
#print(ax1)
HPI_data['TX1yr'] = HPI_data['TX'].resample('A',how="mean")
print(HPI_data[['TX1yr','TX']].head())
#HPI_data.dropna(inplace=True)
HPI_data.fillna(value=-9999,inplace=True)
print(HPI_data[['TX1yr','TX']].head())

HPI_data[['TX1yr','TX']].plot(ax=ax1)

plt.legend(loc=4);
plt.show()