# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:59:27 2021

Extract Data from Ensemble Data - Kiko

@author: mi292519
"""

import os 
# import numpy as np
import pandas as pd 
# import seaborn as sns
import scipy.io as sio
from datetime import datetime
from datetime import timedelta
# import matplotlib.pyplot as plt

dir_in = "G:\\05_era5\\kikoStuff\\ensembleData"
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
    

#load files
for ii in range(len(ensList)):
    print(ii)
    dat = sio.loadmat(ensList[ii])
    
    #get time 
    datTime = pd.DataFrame(dat['time'])
    
    getTime = lambda x: datenum_to_datetime(x)
    ensTime = pd.DataFrame(list(map(getTime, datTime[0])))
    
    getTimeStr = lambda x: str(x)
    ensTime = pd.DataFrame(list(map(getTimeStr, ensTime[0])))
    
    getYMD = lambda x: x.split()[0]
    ensTime = pd.DataFrame(list(map(getYMD, ensTime[0])))
    




