# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:33:45 2021

eXtract slp and wsp within 2x2 grid 
apply it for 100 ensemble members

@author: Michael Tadesse
"""
import os 
import pandas as pd 
import scipy.io as sio
from datetime import datetime
from datetime import timedelta

dir_in = "G:\\05_era5\\kikoStuff\\ensembleData"
dir_tg = "G:\\05_era5\\kikoStuff\\06-annualMax"
dir_out = "G:\\05_era5\\kikoStuff\\ensFiles\\eXtraction"

os.chdir(dir_in)

ensList = os.listdir()


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
           
def getMesh(lon, lat, tgLon, tgLat):
    """
    get a 2x2 mesh lonlat
    """
    x = (lat >= tgLat-2) & (lat <= tgLat+2);
    y = (lon >= tgLon-2) & (lon <= tgLon+2);
    xy = (x == True) & (x == y);
    # (xy[xy == True]).count(axis = 1) #count True values
    return xy;

def subsetPredictor(mesh, slp, wsp):
    """
    subset predictor in 2x2 mesh
    
    * get lat - get lon - subset based on tg
    * get intersection of lon lat subset
    * simply subset predictor with intersection
    
    """
    newSLP = pd.DataFrame(slp[mesh]).T;
    newWSP = pd.DataFrame(wsp[mesh]).T;
    
    return newSLP, newWSP;


def eXtract():
    """
    extract slp and wsp from 100 ensemble
    """
    for ens in ensList:
        
        os.chdir(dir_in)
        
        print(ens)
        ensName = ens.split('daily_')[1].split('.mat')[0]
        
        #get time lon lat and predictors
        matFile = sio.loadmat(ens)
        lat = pd.DataFrame(matFile['lat'])
        lon = pd.DataFrame(matFile['lon'])
    
        #get time    
        time = pd.DataFrame(matFile['time'])
        getTime = lambda x: datenum_to_datetime(x)
        time = pd.DataFrame(list(map(getTime, time[0])))
        
        time['date'] = 'nan'
        for ii in range(len(time)):
            time['date'][ii] = \
                datenum_to_datetime(time[0][ii]).strftime('%Y-%m-%d')
    
        #predictors
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
            if ((tgLon > lon.max().max()) | (tgLon < lon.min().min())):
                #way to the east of ens data
                print("tg outiside the longitude bound")
                continue 
            elif ((tgLat > lat.max().max()) | (tgLat < lat.min().min())):
                #way to the west of ens data
                print("tg outside the latitude bound")
                continue
            
            #do extraction 
            mesh = getMesh(lon, lat, tgLon, tgLat);
            tgSLP = subsetPredictor(mesh, slp, wsp)[0];
            tgWSP = subsetPredictor(mesh, slp, wsp)[1];
            
            #concatenate time
            tgTime = time['date'];
            tgSLP = pd.concat([tgTime, tgSLP], axis = 1)
            tgWSP = pd.concat([tgTime, tgWSP], axis = 1)
    
            #create folders 
            os.chdir(dir_out)
            try:    
                os.makedirs(tg)
                os.chdir(tg)
                
                os.makedirs(ensName)
                os.chdir(ensName)
                tgName= tg.split('.csv')[0]
                
                tgSLP.to_csv(tgName+"SLP.csv")
                tgWSP.to_csv(tgName+"WSP.csv")
                
            except FileExistsError:
                os.chdir(tg)
                
                os.makedirs(ensName)
                os.chdir(ensName)
    
                
                tgName= tg.split('.csv')[0]
                
                tgSLP.to_csv(tgName+"SLP.csv")
                tgWSP.to_csv(tgName+"WSP.csv")
        
        


    


    