# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:08:34 2016

@author: CJ

generatet a table about US province house price
"""

import quandl
import pandas as pd
import pickle

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
def grab_initital_state_data():
    states = state_list()
    main_df =  pd.DataFrame()
    for abbv in states:
            #print(abbv)
            #print("FMAC/HPI_"+str(abbv))
            query = "FMAC/HPI_"+str(abbv)
            print(query)
            df = quandl.get(query)
            df.rename(columns={'Value':str(abbv)}, inplace=True)
            print(df.head())
           
            
            if main_df.empty:
                main_df = df
            else:
                    main_df = main_df.join(df)
                    
    print(main_df)
    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close() 
                    
#print(main_df.head())

grab_initital_state_data()
