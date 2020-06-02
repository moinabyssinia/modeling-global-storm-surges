# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 10:00:00 2020

MERRAv2 netCDF extraction script

@author: Michael Tadesse
""" 
import os 
import pandas as pd
from d_merra_define_grid import Coordinate, findPixels, findindx
from c_merra_read_netcdf import readnetcdf
from f_merra_subset import subsetter

def extract_data(delta):
    """
    This is the master function that calls subsequent functions
    to extract uwnd, vwnd, slp for the specified
    tide gauges
    
    delta: distance (in degrees) from the tide gauge
    """
    
    print('Delta =  {}'.format(delta), '\n')
    
    #defining the folders for predictors
    dir_in = "D:\\data\\MERRAv2\\data"
    surge_path = "D:\data\obs_surge"
    csv_path = "G:\\04_merra\\merra_localized"
    
    #cd to the obs_surge dir to get TG information
    os.chdir(surge_path)
    tg_list = os.listdir()
    
    #cd to the obs_surge dir to get TG information
    os.chdir(dir_in)
    years = os.listdir()
    
    #################################
    #looping through the year folders
    #################################

    for yr in years:
        os.chdir(dir_in)
        print(yr, '\n')
        os.chdir(os.path.join(dir_in, yr))

        ####################################
        #looping through the daily .nc files
        ####################################

        for dd in os.listdir():
            
            os.chdir(os.path.join(dir_in, yr)) #back to the predictor folder
            print(dd, '\n')
            
            #########################################
            #get netcdf components  - predictor file            
            #########################################

            nc_file = readnetcdf(dd)
            lon, lat, time, predSLP, predU10, predV10 = \
                nc_file[0], nc_file[1], nc_file[2], nc_file[3], nc_file[4]\
                    , nc_file[5]
            
            
            #looping through individual tide gauges
            for t in range(0, len(tg_list)):
                
                #the name of the tide gauge - for saving purposes
                # tg = tg_list[t].split('.mat.mat.csv')[0] 
                tg = tg_list[t]
                
                #extract lon and lat data from surge csv file
                print(tg, '\n')
                os.chdir(surge_path)
                
                if os.stat(tg).st_size == 0:
                    print('\n', "This tide gauge has no surge data!", '\n')
                    continue
                
                surge = pd.read_csv(tg, header = None)
                #surge_with_date = add_date(surge)
        
                #define tide gauge coordinate(lon, lat)
                tg_cord = Coordinate(surge.iloc[0,0], surge.iloc[0,1])
                
                
                #find closest grid points and their indices
                close_grids = findPixels(tg_cord, delta, lon, lat)
                ind_grids = findindx(close_grids, lon, lat)                
                
                
                #loop through preds#
                
                #subset predictor on selected grid size
                pred_new = subsetter(pred, ind_grids, time)
                
                #create directories to save pred_new
                os.chdir(csv_path)
                
                #tide gauge directory
                tg_name = tg.split('.mat.mat.csv')[0]
                
                try:
                    os.makedirs(tg_name)
                    os.chdir(tg_name) #cd to it after creating it
                except FileExistsError:
                    #directory already exists
                    os.chdir(tg_name)
                
                # #delta directory
                # del_name = 'D' + str(delta)
                
                # try:
                #     os.makedirs(del_name)
                #     os.chdir(del_name) #cd to it after creating it
                # except FileExistsError:
                #     #directory already exists
                #     os.chdir(del_name)
                
                #predictor directory
                pred_name  = pf
                
                try:
                    os.makedirs(pred_name)
                    os.chdir(pred_name) #cd to it after creating it
                except FileExistsError:
                    #directory already exists
                    os.chdir(pred_name)
                
                #save as csv
                if py.startswith('prmsl'):
                    yr_name = py.split('.')[1]
                else:
                    yr_name = py.split('.')[2]
                save_name = '_'.join([tg_name, pred_name, yr_name])\
                    + ".csv"
                pred_new.to_csv(save_name)
            
            #return to the predictor directory
            os.chdir(nc_path[pf])
                        
        