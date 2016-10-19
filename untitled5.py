# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:48:02 2016

@author: CJ
"""


import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,3]
playing = [8,5,7,8,12]

slices = [7,2,3,12]
activities = ['sleeping','eating','working','playing']

cols = ['c','m','r','k']
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0),
        autopct='%1.1f%%')


plt.show()