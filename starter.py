# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:30:37 2019

@author: Michael Tadesse
"""

import os 
import pandas as pd

script_path = "C:/Users/WahlInstall/Documents/ml_project_v3/scripts/modeling_storm_surge"
os.chdir(script_path)

data_path = "E:\data\era_interim" #where netcdf files are stored

from define_grid import Coordinate, findPixels, findindx
from read_netcdf_v2 import readnetcdf
from subset import subsetter
from surgets import add_date

#define tide gauge


tg_cord = Coordinate(8.7167, 53.867)


#read netcdf files

os.chdir(data_path)
files = pd.DataFrame(os.listdir())


nc_files = readnetcdf(data_path, 'vwnd', '2003_2006')
lon, lat, time, pred = nc_files[0], nc_files[1], nc_files[2], nc_files[3]


#subset lon/lat/pred

close_grids = findPixels(tg_cord, 5, lon, lat)
ind_grids = findindx(close_grids, lon, lat)
pred_sub = subsetter(pred, ind_grids, time)


#choose surge time series

surge = pd.read_csv('cuxhaven-germany-bsh.mat.mat.csv', header=None)
surge_with_date = add_date(surge)


#this is to be done last
#merge predictors and predictand with 'date' as a key

pred_surge = pd.merge(pred_sub, surge_with_date.iloc[:,8:10], \
                      on = "date", how = "inner")

    