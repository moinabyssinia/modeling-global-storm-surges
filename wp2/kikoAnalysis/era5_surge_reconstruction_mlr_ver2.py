# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:51:30 2020

----------------------------------------------------
This program is designed to reconstruct ERA-Five daily
maximum surge using MLR
----------------------------------------------------

@author: Michael Tadesse
"""
#import packages
import os
import numpy as np
import pandas as pd
from sklearn import metrics
from scipy import stats
import statsmodels.api as sm
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler

#defining directories    
dir_in = 'G:\\05_era5\\kikoStuff\\combinedPred'
dir_out = 'G:\\05_era5\\kikoStuff\\test'
surge_path = 'G:\\05_era5\\kikoStuff\\05_dmax_surge_georef'

def reconstruct():
    """
    run KFOLD method for regression 
    """
    
    #cd to the lagged predictors directory
    os.chdir(dir_in)
    

    #looping through 
    for tg in range(len(os.listdir())):
        
        os.chdir(dir_in)

        tg_name = os.listdir()[tg]
        print(tg, tg_name)
        
        #load predictor
        pred = pd.read_csv(tg_name)
        pred.drop('Unnamed: 0', axis = 1, inplace = True)
        
        #add squared and cubed wind terms (as in WPI model)
        pickTerms = lambda x: x.startswith('wnd')
        wndTerms = pred.columns[list(map(pickTerms, pred.columns))]
        wnd_sqr = pred[wndTerms]**2
        wnd_cbd = pred[wndTerms]**3
        pred = pd.concat([pred, wnd_sqr, wnd_cbd], axis = 1)

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
        
        #remove duplicated surge rows
        surge.drop(surge[surge['date'].duplicated()].index, axis = 0, inplace = True)
        surge.reset_index(inplace = True)
        surge.drop('index', axis = 1, inplace = True)
        
        
        #adjust surge time format to match that of pred
        time_str = lambda x: x.split()[0]
        surge_time = pd.DataFrame(list(map(time_str, surge['date'])), columns = ['date'])
        # time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        surge_new = pd.concat([surge_time, surge[['surge', 'lon', 'lat']]], axis = 1)
    
        #merge predictors and surge to find common time frame
        pred_surge = pd.merge(pred_standardized, surge_new.iloc[:,:2], on='date', how='right')
        pred_surge.sort_values(by = 'date', inplace = True)
        
        #find rows that have nans and remove them
        row_nan = pred_surge[pred_surge.isna().any(axis =1)]
        pred_surge.drop(row_nan.index, axis = 0, inplace = True)
        pred_surge.reset_index(inplace = True)
        pred_surge.drop('index', axis = 1, inplace = True)
        
        
        #in case pred and surge don't overlap
        if pred_surge.shape[0] == 0:
            print('-'*80)
            print('Predictors and Surge don''t overlap')
            print('-'*80)
            continue

        
        #prepare data for training/testing
        X = pred_surge.iloc[:,1:-1]
        y = pd.DataFrame(pred_surge['surge'])
        y = y.reset_index()
        y.drop(['index'], axis = 1, inplace = True)
        
        #apply PCA
        pca = PCA(.95)
        pca.fit(X)
        X_pca = pca.transform(X)
        
        
        num_pc = X_pca.shape[1] #number of principal components
        longitude = surge['lon'][0]
        latitude = surge['lat'][0]
        
        #surge reconstruction
        pred_for_recon = pred[~pred.isna().any(axis = 1)]
        pred_for_recon = pred_for_recon.reset_index().drop('index', axis = 1)
        
        
        #standardize predictor data
        dat = pred_for_recon.iloc[:,1:]
        scaler = StandardScaler()
        print(scaler.fit(dat))
        dat_standardized = pd.DataFrame(scaler.transform(dat), \
                                        columns = dat.columns)
        pred_standardized = pd.concat([pred_for_recon['date'], dat_standardized], axis = 1)
        
        X_recon = pred_standardized.iloc[:, 1:]
        
        #apply PCA
        pca = PCA(num_pc) #use the same number of PCs used for training
        pca.fit(X_recon)
        X_pca_recon = pca.transform(X_recon)
    
    
        #model preparation
        #first train model using observed surge and corresponding predictors
        X_pca = sm.add_constant(X_pca)
        est = sm.OLS(y['surge'], X_pca).fit()
        
        #predict with X_recon and get 95% prediction interval
        X_pca_recon = sm.add_constant(X_pca_recon)
        predictions = est.get_prediction(X_pca_recon).summary_frame(alpha = 0.05)
        
        #drop confidence interval and mean_se columns 
        predictions.drop(['mean_se', 'mean_ci_lower','mean_ci_upper'], \
                         axis = 1, inplace = True)
        
        #final dataframe
        final_dat = pd.concat([pred_standardized['date'], predictions], axis = 1)
        final_dat['lon'] = longitude
        final_dat['lat'] = latitude
        final_dat.columns = ['date', 'surge_reconsturcted', 'pred_int_lower',\
                             'pred_int_upper', 'lon', 'lat']


        #save df as cs - in case of interruption
        os.chdir(dir_out)
        final_dat.to_csv(tg_name)
        
        #cd to dir_in
        os.chdir(dir_in)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        