# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:27:40 2016

@author: CJ
"""

import matplotlib.pyplot as plt
import csv
import numpy as np
x=[]
y=[]

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
    

plt.plot(x,y,label='loaded from the file')
plt.show()
x , y = np.loadtxt('example.txt',delimiter=',',unpack=True)

plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()