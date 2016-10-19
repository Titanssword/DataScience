# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:46:11 2016

@author: CJ
"""

import matplotlib.pyplot as plt
import numpy as np
import quandl
import matplotlib.dates as mdates
from pandas.io.data import DataReader
df=DataReader('TSLA','yahoo')
#print(df)


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

ax1.plot(df['Open'])
print(df['Open'])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
    
