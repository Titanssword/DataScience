# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:20:22 2016

@author: CJ
"""

import quandl
import pandas as pd
import html5lib
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
df = pd.read_csv('Students.csv')
print(df.head())

plt.hist(df['Height'],100)
plt.show()

print(df['Height'])
ArrayHeight = np.array(df['Height'])
print(ArrayHeight)

