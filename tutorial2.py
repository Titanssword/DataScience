# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:13:13 2016

@author: CJ
"""
import pandas as pd
df = pd.read_csv('MOHRSS-0102.csv')

#print(df.head())

"""
Date  Total Population 10000 persons  Male Population  \
0  2010-12-31                        134091.0          68748.0   
1  2009-12-31                        133450.0          68647.0   
2  2008-12-31                        132802.0          68357.0   
3  2007-12-31                        132129.0          68048.0   
4  2006-12-31                        131448.0          67728.0   
"""

df.set_index('Date')
df.to_csv('to_csv2.csv')

df2 = pd.read_csv('to_csv2.csv')
#print(df2.head())
#print(df2['Total Population 10000 persons'].head())

df.colums = ['Austion_HPI']
#print(df.head())

#print(df.head())
df.to_html('example.html')

df = pd.read_csv('MOHRSS-0102.csv',names=['Date','Total Population 10000 persons'])
#print(df.head())

