# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:19:58 2016

@author: CJ
"""
"""
获取yahoo的股票
"""
import pandas as pd
import datetime
import pandas.io.data as web

import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)
#从互联网获取数据
df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()