# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:44:08 2016

@author: CJ
"""

import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]
plt.plot(x,y,label='fisrt')
plt.plot(x2,y2,label='second')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('WTF')
plt.legend()
plt.show()