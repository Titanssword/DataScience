# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:59:35 2016

@author: CJ
"""

from numpy import array
from numpy.random import normal
import quandl
import pandas as pd
import html5lib
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
def genData():
     heights = []
     weights = []
     grades = []
     N = 10000
 
     for i in range(N):
         while True:
             #身高服从均值172，标准差为6的正态分布
             height = normal(172, 6)
             if 0 < height: break
         while True:
             #体重由身高作为自变量的线性回归模型产生，误差服从标准正态分布
             weight = (height - 80) * 0.7 + normal(0, 1)
             if 0 < weight: break
         while True:
             #分数服从均值为70，标准差为15的正态分布
             score = normal(70, 15)
             if 0 <= score and score <= 100:
                 grade = 'E' if score < 60 else ('D' if score < 70 else ('C' if score < 80 else ('B' if score < 90 else 'A')))
                 break
         heights.append(height)
         weights.append(weight)
         grades.append(grade)
     return array(heights), array(weights), array(grades)
 
heights, weights, grades = genData()
print(heights)
print(weights)
print(grades)
df = pd.DataFrame()
df['Height']=heights
df['Weight']=weights
df['Grade']=grades

"""
temp = np.array(heights,weights,grades)
indexs = [x in length(heights)]
print(indexs)
df = pd.DataFrame(temp,index=indexs,colums=['Height','Weight','Grade'])
print(df.head())
"""
print(df.head())
df.to_csv('Students.csv')