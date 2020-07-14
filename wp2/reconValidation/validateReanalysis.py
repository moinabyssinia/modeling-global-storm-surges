# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:00:00 2020

To validate reconstruction between 1980-2010

@author: Michael Tadesse
"""
#import libraries
import os 
import pandas as pd 

def getFiles(data):
    """
    this function gets the reconstruction time
    series and the observed surge time series

    data = ["twcr", "era20c", "eraint", "merra"]
    """
    reconPath = {
        "twcr": "E:\\03_20cr\\08_20cr_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "era20c": "F:\\02_era20C\\08_era20C_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "eraint": "F:\\01_erainterim\\08_eraint_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "merra": "G:\\04_merra\\08_merra_surge_reconstruction\\bestReconstruction\\surgeReconstructed"
        }

    surgePath = "D:\\data\\allReconstructions\\05_dmax_surge_georef"

    os.chdir(reconPath[data])

    tg_list = os.listdir()    

    for ii in range(0, 2):
        tg = tg_list[ii]
        print(tg, '\n')
        #get reconstruction
        os.chdir(reconPath[data])
        reconSurge = pd.read_csv(tg)
        #get surge time series
        os.chdir(surgePath)
        obsSurge = pd.read_csv(tg)
    
    # print(reconSurge.head())
    # print(obsSurge.head())
        #implement subsetting
        subsetFiles(reconSurge, obsSurge)

def subsetFiles(reconSurge, obsSurge):
    """
    this function subsets the reconstructed surge
    and observed surge for the 1980-2010 period
    """
    #get extra column that is only ymd
    ymdMaker = lambda x: x[0:10]
    reconSurge['ymd'] = pd.DataFrame(list(map(ymdMaker, reconSurge['date'])))
    obsSurge['ymd'] = pd.DataFrame(list(map(ymdMaker, obsSurge['date'])))

    reconSurge = reconSurge[(reconSurge['ymd'] >= '1980-01-03') & (reconSurge['ymd'] <= '2011-01-01')]
    obsSurge = obsSurge[(obsSurge['ymd'] >= '1980-01-03') & (obsSurge['ymd'] <= '2011-01-01')]
    
    print(reconSurge.head())
    print(obsSurge.head())
