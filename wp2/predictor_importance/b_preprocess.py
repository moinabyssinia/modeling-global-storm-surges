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
from c_train_test_regression import lr_reg
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split



def preprocess(case):
    """
    This function loads lagged predictors - loads surge time series 
    standardizes predictors - prepares the predictors belonging to each case
    prepare data for training/testing
    
    base_case = wnd_u, wnd_v, slp
    prcp_case =  wnd_u, wnd_v, slp, prcp
    sst_case =  wnd_u, wnd_v, slp, sst
    
    
    output: training and testing predictor and predictand data
    """

    
    #defining directories    
    dir_in = 'F:\\eraint_lagged_predictors'
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
        row_nan = pred_surge[pred_surge.isna().any(axis =1)]
        pred_surge.drop(row_nan.index, axis = 0, inplace = True)
        
       
        #remove predictors of choice - as per chosen case
        test = lambda x: x.startswith(ii)
        for ii in pred_case[case]:
            print(case,'- now removing: ' , pred_case[case])
            remove_cols = pred_surge.columns[list(map(test, pred_surge.columns))]
            # pred_remove = pred_surge.loc[:, remove_cols]
            pred_surge = pred_surge.drop(remove_cols, axis = 1)
        
        
        
        #split data to training and testing 
        X = pred_surge.iloc[:,1:-1]
        y = pred_surge['surge']
        
        X_train, X_test, y_train, y_test, = \
            train_test_split(X,y, test_size = 0.2, random_state = 101)
        
        
        #empty dataframe for model validation
        df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'corrn', 'rmse'])
        
        #model validation
        [corrn, rmse] = lr_reg(X_train, X_test, y_train, y_test)
        lon = surge.lon[0]
        lat = surge.lat[0]
        
        df.loc[tg,  :] = [tg_name, lon, lat, corrn, rmse]
        
    return df
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    