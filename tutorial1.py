# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:31:40 2016

@author: CJ
"""
import pandas as pd
import datetime
import pandas.io.data as web
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}
df = pd.DataFrame(web_stats)

print(df)

"""
   Bounce Rate  Day  Visitors
0           65    1        43
1           67    2        34
2           78    3        65
3           65    4        56
4           45    5        29
5           52    6        76
"""

print(df.set_index('Day'))

"""
     Bounce Rate  Visitors
Day                       
1             65        43
2             67        34
3             78        65
4             65        56
5             45        29
6             52        76
"""

print(df.Visitors)

"""
0    43
1    34
2    65
3    56
4    29
5    76
"""

print(df[['Bounce Rate','Visitors']])
"""
   Bounce Rate  Visitors
0           65        43
1           67        34
2           78        65
3           65        56
4           45        29
5           52        76
"""

print(df.Visitors.tolist())
"""
[43, 34, 65, 56, 29, 76]
"""

print(np.array(df[['Bounce Rate','Visitors']]))
"""
[[65 43]
 [67 34]
 [78 65]
 [65 56]
 [45 29]
 [52 76]]
"""
df2 = pd.DataFrame(np.array(df[['Bounce Rate','Visitors']]))

print(df2)
