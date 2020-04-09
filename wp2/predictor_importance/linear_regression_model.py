# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:57:21 2020

This script standardizes the predictor data 
and trains a linear regression model

This script might be used for reconstructing surges also

*Notice that K-Fold CV was not used and thus reconstruction can not be done here
Adjust script for later use - if reconstruction is needed

@author: Michael Tadesse
"""

import os 
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split




dir_in = 'F:\\eraint_lagged_predictors'
# dir_out = ''
surge_path = 'F:\\dmax_surge_georef'


#load predictors
#cd to the lagged predictors directory

os.chdir(dir_in)

#looping through TGs
for tg in range(len(os.listdir())):
    print(tg)
    
    tg_name = os.listdir()[tg]
    
    #load predictor
    pred = pd.read_csv(tg_name)
    pred.drop('Unnamed: 0', axis = 1, inplace = True)
    
    #standardize predictor data
    dat = pred.iloc[:,1:]
    scaler = StandardScaler()
    print(scaler.fit(dat))
    dat_standardized = pd.DataFrame(scaler.transform(dat), \
                                    columns = dat.columns)
    pred_standardized = pd.concat([pred['date'], dat_standardized], axis = 1)
    
    #load surge data
    os.chdir(surge_path)
    surge = pd.read_csv(tg_name)
    surge.drop('Unnamed: 0', axis = 1, inplace = True)
    
    
    #adjust surge time format to match that of pred
    time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d'))
    surge_time = pd.DataFrame(list(map(time_str, surge['ymd'])), columns = ['date'])
    surge_new = pd.concat([surge_time, surge[['surge', 'lon', 'lat']]], axis = 1)

    #merge predictors and surge to find common time frame
    pred_surge = pd.merge(pred_standardized, surge_new.iloc[:,:2], on='date', how='right')
    pred_surge.sort_values(by = 'date', inplace = True)
    
    #find rows that have nans and remove them
    row_nan = pred_surge[pred_surge.iloc[:,1].isnull()]
    pred_surge.drop(row_nan.index, axis = 0, inplace = True)
    
   
    #remove predictors of choice
    pred_surge
    
    #split data to training and testing 
    X = pred_surge.iloc[:,1:-1]
    y = pred_surge['surge']
    
    X_train, X_test, y_train, y_test, = \
        train_test_split(X,y, test_size = 0.2, random_state = 101)
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    