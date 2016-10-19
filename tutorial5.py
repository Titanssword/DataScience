# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:05:55 2016

@author: CJ
"""

import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

print(pd.merge(df1,df2,on = "HPI"))
print(df1)
print(df2)

"""
 HPI  Int_rate  US_GDP_Thousands
2001   80         2                50
2002   85         3                55
2003   88         2                65
2004   85         2                55
      HPI  Int_rate  US_GDP_Thousands
2005   80         2                50
2006   85         3                55
2007   88         2                65
2008   85         2                55
HPI  Int_rate_x  US_GDP_Thousands_x  Int_rate_y  US_GDP_Thousands_y
0   80           2                  50           2                  50
1   85           3                  55           3                  55
2   85           3                  55           2                  55
3   85           2                  55           3                  55
4   85           2                  55           2                  55
5   88           2                  65           2                  65
"""

print(pd.merge(df1,df2,on=['HPI','Int_rate']))

"""
merge means index doex not matter to you
 HPI  Int_rate  US_GDP_Thousands_x  US_GDP_Thousands_y
0   80         2                  50                  50
1   85         3                  55                  55
2   88         2                  65                  65
3   85         2                  55                  55
"""

df1.set_index('HPI',inplace=True)
df3.set_index('HPI',inplace=True)

joined = df1.join(df3)
print(joined)
"""
join means index does matter to you 
Int_rate  US_GDP_Thousands  Low_tier_HPI  Unemployment
HPI                                                        
80          2                50            50             7
85          3                55            52             8
85          3                55            53             6
85          2                55            52             8
85          2                55            53             6
88          2                65            50             9
"""



df4 = pd.DataFrame({
                    'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]
                    
                    })

df5 = pd.DataFrame({
                    'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]
                    })



merged = pd.merge(df4,df5, on='Year')
print(merged)
"""

how ='inner'
Int_rate  US_GDP_Thousands  Year  Low_tier_HPI  Unemployment
0         2                50  2001            50             7
1         2                65  2003            52             8
2         2                55  2004            50             9

how = 'left'
how = 'right'
how = 'outer'
"""















