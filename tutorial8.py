# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:55:08 2016

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
print(ax1)
TX1yr = HPI_data['TX'].resample('A',how="mean")
print(TX1yr.head())
HPI_data['TX'].plot(ax=ax1 ,label='Monthly TX HPI')
TX1yr.plot(ax=ax1,label='Monthly TX HPI')
plt.legend(loc=4);
plt.show()