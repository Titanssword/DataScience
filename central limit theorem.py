# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 21:03:27 2016

@author: CJ
"""

import pandas.io.data as web
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from scipy.stats import norm

df = pd.read_csv('D:python/MOHRSS-0102.csv')
print(df)
df['Total Population 10000 persons'].plot()

plt.show()
data = df['Total Population 10000 persons']

print(data)
"""
n是多少次
m是取出来几个
"""
n=1000
m=10
array = np.zeros((n,m))
print(array)
i=0
while i < n:
    temp = np.random.choice(data,m)
    #print('一次取出的值'+temp)
    array[i]=temp
    i=i+1
print(array)

sum1 = np.sum(array,axis=1)
print(sum1)
sum1=np.int_(sum1)

miu = m*np.mean(sum1)
si = np.var(sum1)
sigma = np.sqrt(m*si)
print(miu)
print(sigma)
x = np.linspace(8000000,12000000,1000000)

y = norm.pdf(x,miu,sigma)

plt.plot(x,y,'r--')
"""
convert 2D float numpy array to 2D int numpy array?

"""
print(sum1)

h = np.histogram(sum1,n/10)
"""
后面的是用来调节柱子的数量，选取合适的数量进行统计
"""

x = np.linspace(0,n/10)
y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-1.0*(x-miu)**2/(2.0*sigma**2))

line1=plt.plot(x,y,'r--')
plt.show()
print(h[0])
print(h[0]/(m*1.0))
val = np.arange(len(h[0]))
bar1 = plt.bar(val,h[0]/(n*1.0))
plt.show()

                 