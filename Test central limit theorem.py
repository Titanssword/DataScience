# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 18:57:06 2016

@author: CJ
"""

import pandas.io.data as web
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
"""
style.use('ggplot')

start = datetime.datetime(2000, 1, 1)

end = datetime.datetime(2016, 10, 7)

f = web.DataReader("F", 'yahoo', start, end)

print(f)

f['Adj Close'].plot()

plt.show()

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounce_Rate':[54,35,23,65,34,23]
             }
df = pd.DataFrame(web_stats)

print(df)
"""
#print(np.array(df[['Day','Visitors']]))
"""
n是多少次
m是取出来几个
"""
n=10
m=10
s = np.random.randint(0,2,(n,m))
print(s)
sum1 = np.sum(s,axis=1)
#如果axis= 1 横向相加
"""

[[1 1 1 1 1 0 0 1 0 1]
 [1 1 1 1 0 0 0 1 0 1]
 [1 0 1 0 0 0 1 1 0 1]
 [1 1 1 0 1 0 1 0 1 0]
 [1 0 1 0 0 1 1 0 1 1]
 [0 1 1 0 1 0 0 0 1 0]
 [0 1 0 1 1 0 0 0 1 0]
 [0 0 0 0 1 1 0 1 1 1]
 [0 1 0 0 0 1 0 0 0 1]
 [0 1 0 1 1 1 1 1 0 1]]
 
 
[7 6 5 6 6 4 4 5 3 7]
"""
print(sum1)

sum2 = np.sum(s,axis=0)
"""

[[1 1 0 1 0 0 0 1 0 1]
 [1 1 1 1 0 1 1 0 0 1]
 [0 1 1 1 0 1 0 1 0 0]
 [0 1 0 1 0 0 0 1 1 0]
 [0 0 0 1 1 0 0 1 0 0]
 [1 0 1 0 1 1 1 0 1 0]
 [0 0 1 1 0 0 0 1 1 0]
 [0 0 0 0 1 1 1 1 1 1]
 [0 0 1 1 0 0 1 1 0 1]
 [1 0 0 0 1 0 0 0 0 1]]
[5 7 5 4 3 6 4 6 5 3]
[4 4 5 7 4 4 4 7 4 5]
如果axis=0 纵列相加
"""
print(sum2)

sq=np.sqrt([1,4,9])
"""

数组开根号
返回数组
[ 1.  2.  3.]
"""

print(sq)
"""
画出柱形图
[4 4 4 5 4 5 7 3 5 5]
"""
h = np.histogram(sum1, n)
val =h[1][:-1]
bar1 = plt.bar(val,h[0]/(n*1.0))
"""
计算print(h[0]/(m*1.0))每个值出现的概率
h[0]每个值出现的次数

val=[ 0  1  2  3  4  5  6  7  8  9 10]
"""


plt.show()
print(sum1)
print(h[0]/(m*1.0))
print(h[0])
print(val)
"""
x = np.arange(-10, 10, 0.1);
y = np.sin(x)
plt.bar(x, y)

bar x表示左边界，右边界,清晰度
y 表示x每个点对应的值
"""

"""
y=list(range(1,10))
slice = random.sample(y, 5)  #从list中随机获取5个元素，作为一个片断返回  
print (slice)  
print (y) #原有序列并没有改变。

[8, 5, 6, 2, 9] 
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
