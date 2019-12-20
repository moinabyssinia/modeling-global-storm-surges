# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:41:05 2019

@author: Michael Tadesse
"""
import os 
import pandas as pd
from define_grid import Coordinate
from surgets import add_date
from compiler import compile_predictors

def extract_data(delta):
    """
    This is the master function that calls subsequent function
    to extract uwnd, vwnd, slp, and observed surge for the specified
    tide gauges
    
    delta: distance (in degrees) from the tide gauge
    """
    nc_path = "E:\data\era_interim" #where netcdf files are stored
    surge_path = "E:\data\obs_surge"
    csv_path = "E:\data\pred_and_surge"
    
    #cd to the obs_surge dir
    os.chdir(surge_path)
    
    for tg in os.listdir():
        
        t0 = time.time()
        #extract lon and lat data
        print(tg, '\n')
        
        os.chdir(surge_path)
        surge = pd.read_csv(tg, header = None)
        surge_with_date = add_date(surge)
        
        #define tide gauge coordinate(lon, lat)
        tg_cord = Coordinate(surge.iloc[0,0], surge.iloc[0,1])
        
        #get netcdf files
        nc_files = compile_predictors(tg_cord, delta, nc_path)

        #concatenated predictors
        pred_combo = nc_files[3]
        
        #concatenate predictors with obs_surge
        pred_and_surge = pd.merge(pred_combo, surge_with_date.iloc[:,8:], \
                          on="date", how="inner")
        
        #save as csv
        os.chdir(csv_path)
        save_name = tg.split('.mat.mat.csv')[0] + ".csv"
        pred_and_surge.to_csv(save_name)

        print(time.time() - t0)
        
        