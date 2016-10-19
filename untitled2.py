# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:04:09 2016

@author: CJ
"""

import matplotlib.pyplot as plt
import numpy as np
x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x,y,label='Bars1')
plt.bar(x2,y2,label='Bars2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('WTF')
plt.legend()
plt.show()

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,122,130,111,114,113,80,75,65,54,33,43,42,48]
ids = [x for x in range(len(population_ages))]
#print(ids)
plt.bar(ids,population_ages)
plt.show()
bins = [0,10,20,30,40,50,60,70,80,90,100,120,130]



plt.hist(population_ages,bins)

plt.show()


