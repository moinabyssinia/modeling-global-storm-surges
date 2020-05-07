# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:25:34 2020

This script compares the kfold validation 
of the linear regression and Random Forest 
and chooses the model that should be used to 
reconstruct the surge for the given tide gauge

@author: Michael Tadesse
"""


def chooseModel():
    
    #import packages
    import os
    import pandas as pd
    
    dir_in = 'F:\\06_eraint_results\\model_fitting'
    dir_out_surge = 'F:\\08_eraint_surge_reconstruction\\bestReconstruction\\surgeReconstruced'
    dir_out_metadata = 'F:\\08_eraint_surge_reconstruction\\bestReconstruction\\metaData'
    
    #read kfold validation csvs
    os.chdir(dir_in)
    lr = pd.read_csv('eraint_lrreg_kfold.csv')
    rf = pd.read_csv('eraint_randForest_kfold.csv')
    
    #merge the two csvs
    comp = pd.merge(lr, rf, on = 'tg', how = 'right')
    comp = comp[['tg', 'lon_x', 'lat_x', 'num_year_x', 'num_95pcs_x',
       'corrn_x', 'rmse_x', 'corrn_y', 'rmse_y']]
    comp.columns = ['tg', 'lon', 'lat', 'num_year', 'num_95pcs',
       'corrn_lr', 'rmse_lr', 'corrn_rf', 'rmse_rf']
    
    #filter comp based on RMSE results
    comp[comp['rmse_lr'] <= comp['rmse_rf']]