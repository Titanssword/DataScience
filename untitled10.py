# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:22:04 2016

@author: CJ
"""

import quandl
import pandas as pd
import html5lib
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv('BCHARTS-BTCNCNY.csv')
print(df.head())
Date=df['Date']
HPI = df['Close']
print(Date)
print(HPI)
plt.hist(HPI,100)
plt.show()