# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:38:44 2016

@author: CJ
"""
"""
using "pip install quandl " to install quandl modules
"""
import quandl
import pandas as pd
import html5lib

"""
get the dataframe from the quandl by using the authtoken
"""

df = quandl.get("SWA/1B", authtoken="FJF42_NFf8551EUVpR3W")

print(df.head())
f_states=   pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
"""
if "html5lib not found, please install it" happened
use this:
    pip install pandas
pip install lxml
pip install html5lib
pip install BeautifulSoup4
"""
print(f_states[0])

for abbv in f_states[0][0][1:]:
    print("FMAC/HPI_"+str(abbv)) 
    
"""
      0               1               2                  3
0   Abbreviation      State Name         Capital     Became a State
1             AL         Alabama      Montgomery  December 14, 1819
2             AK          Alaska          Juneau    January 3, 1959
3             AZ         Arizona         Phoenix  February 14, 1912
4             AR        Arkansas     Little Rock      June 15, 1836
5             CA      California      Sacramento  September 9, 1850
6             CO        Colorado          Denver     August 1, 1876
7             CT     Connecticut        Hartford    January 9, 1788
8             DE        Delaware           Dover   December 7, 1787
9             FL         Florida     Tallahassee      March 3, 1845
10            GA         Georgia         Atlanta    January 2, 1788
11            HI          Hawaii        Honolulu    August 21, 1959
12            ID           Idaho           Boise       July 3, 1890
13            IL        Illinois     Springfield   December 3, 1818
14            IN         Indiana    Indianapolis  December 11, 1816
15            IA            Iowa      Des Moines  December 28, 1846
16            KS          Kansas          Topeka   January 29, 1861
17            KY        Kentucky       Frankfort       June 1, 1792
18            LA       Louisiana     Baton Rouge     April 30, 1812
19            ME           Maine         Augusta     March 15, 1820
20            MD        Maryland       Annapolis     April 28, 1788
21            MA   Massachusetts          Boston   February 6, 1788
22            MI        Michigan         Lansing   January 26, 1837
23            MN       Minnesota      Saint Paul       May 11, 1858
24            MS     Mississippi         Jackson  December 10, 1817
25            MO        Missouri  Jefferson City    August 10, 1821
26            MT         Montana          Helena   November 8, 1889
27            NE        Nebraska         Lincoln      March 1, 1867
28            NV          Nevada     Carson City   October 31, 1864
29            NH   New Hampshire         Concord      June 21, 1788
30            NJ      New Jersey         Trenton  December 18, 1787
31            NM      New Mexico        Santa Fe    January 6, 1912
32            NY        New York          Albany      July 26, 1788
33            NC  North Carolina         Raleigh  November 21, 1789
34            ND    North Dakota        Bismarck   November 2, 1889
35            OH            Ohio        Columbus      March 1, 1803
36            OK        Oklahoma   Oklahoma City  November 16, 1907
37            OR          Oregon           Salem  February 14, 1859
38            PA    Pennsylvania      Harrisburg  December 12, 1787
39            RI    Rhode Island      Providence       May 19, 1790
40            SC  South Carolina        Columbia       May 23, 1788
41            SD    South Dakota          Pierre   November 2, 1889
42            TN       Tennessee       Nashville       June 1, 1796
43            TX           Texas          Austin  December 29, 1845
44            UT            Utah  Salt Lake City    January 4, 1896
45            VT         Vermont      Montpelier      March 4, 1791
46            VA        Virginia        Richmond      June 25, 1788
47            WA      Washington         Olympia  November 11, 1889
48            WV   West Virginia      Charleston      June 20, 1863
49            WI       Wisconsin         Madison       May 29, 1848
50            WY         Wyoming        Cheyenne      July 10, 1890
FMAC/HPI_AL
FMAC/HPI_AK
FMAC/HPI_AZ
FMAC/HPI_AR
FMAC/HPI_CA
FMAC/HPI_CO
FMAC/HPI_CT
FMAC/HPI_DE
FMAC/HPI_FL
FMAC/HPI_GA
FMAC/HPI_HI
FMAC/HPI_ID
FMAC/HPI_IL
FMAC/HPI_IN
FMAC/HPI_IA
FMAC/HPI_KS
FMAC/HPI_KY
FMAC/HPI_LA
FMAC/HPI_ME
FMAC/HPI_MD
FMAC/HPI_MA
FMAC/HPI_MI
FMAC/HPI_MN
FMAC/HPI_MS
FMAC/HPI_MO
FMAC/HPI_MT
FMAC/HPI_NE
FMAC/HPI_NV
FMAC/HPI_NH
FMAC/HPI_NJ
FMAC/HPI_NM
FMAC/HPI_NY
FMAC/HPI_NC
FMAC/HPI_ND
FMAC/HPI_OH
FMAC/HPI_OK
FMAC/HPI_OR
FMAC/HPI_PA
FMAC/HPI_RI
FMAC/HPI_SC
FMAC/HPI_SD
FMAC/HPI_TN
FMAC/HPI_TX
FMAC/HPI_UT
FMAC/HPI_VT
FMAC/HPI_VA
FMAC/HPI_WA
FMAC/HPI_WV
FMAC/HPI_WI
FMAC/HPI_WY

"""