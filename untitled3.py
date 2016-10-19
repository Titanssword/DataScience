# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:35:04 2016

@author: CJ
"""

import matplotlib.pyplot as plt
x = [2,4,6,8,10]
y = [6,7,8,2,4]
plt.scatter(x,y,label='skitscat',color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('WTF')
plt.legend()
plt.show()