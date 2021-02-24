# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:33:45 2021

filter lonlatmesh for specific grid size

@author: Michael Tadesse
"""
import os 
import numpy as np
import pandas as pd 
# import seaborn as sns
import scipy.io as sio
from datetime import datetime
from datetime import timedelta
# import matplotlib.pyplot as plt

dir_in = "G:\\05_era5\\kikoStuff\\ensembleData"
dir_tg = "G:\\05_era5\\kikoStuff\\06-annualMax"
dir_out = "G:\\05_era5\\kikoStuff\\ensFiles\\eXtraction"

os.chdir(dir_in)

ensList = os.listdir()

for ens in ensList:
    
    os.chdir(dir_in)
    
    print(ens)
    ensName = ens.split('daily_')[1].split('.mat')[0]
    
    #get time lon lat and predictors
    matFile = sio.loadmat(ens)
    lat = pd.DataFrame(matFile['lat'])
    lon = pd.DataFrame(matFile['lon'])
    slp = matFile['slp']
    wsp = matFile['wsp']
    
    #loop over tide gauges
    os.chdir(dir_tg)
    tgList = os.listdir();
    for tg in tgList:
        
        os.chdir(dir_tg)
        
        tgDat = pd.read_csv(tg)
        tgLon = tgDat['lon'][0]
        tgLat = tgDat['lat'][0]
    
        #filter tgs 
        if (tgLon > lon.max().max()):
            #way to the east of ens data
            print("tg outiside the east bound")
            continue 
        elif (tgLon < lon.min().min()):
            #way to the west of ens data
            print("tg outside the west bound")
            continue
        
        #do extraction 
        
        
        #create folders 
        os.chdir(dir_out)
        try:    
            os.mkdir(tg)
        except FileExistsError:
            os.chdir(tg)
        #save as csv
        
        




#change matlab date to python date
def datenum_to_datetime(datenum):
    """
    Convert Matlab datenum into Python datetime.
    :param datenum: Date in datenum format
    :return:        Datetime object corresponding to datenum.
    """
    days = datenum % 1
    return datetime.fromordinal(int(datenum)) \
           + timedelta(days=days) \
           - timedelta(days=366)
## get tg lon and lat 
def getCoordinates():
    tgLon = -2.715;
    tgLat = 51.511;

def getMesh(lon, lat, tgLon, tgLat):
    """
    get a 2x2 mesh lonlat
    """
    x = (lat >= tgLat-2) & (lat <= tgLat+2);
    y = (lon >= tgLon-2) & (lon <= tgLon+2);
    xy = (x == True) & (x == y);
    # (xy[xy == True]).count(axis = 1) #count True values
    return xy;

def subsetPredictor(mesh):
    """
    subset predictor in 2x2 mesh
    
    * get lat - get lon - subset based on tg
    * get intersection of lon lat subset
    * simply subset predictor with intersection
    
    """
    newSLP = pd.DataFrame(slp[mesh]).T;
    newWSP = pd.DataFrame(wsp[mesh]).T;
    


    