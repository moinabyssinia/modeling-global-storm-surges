# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:36:30 2021

eXtrract time - slp - wnd from ensData

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
os.chdir(dir_in)

ensList = os.listdir()

#size of lon and lat and predictor
nrow = lon.shape[0]
ncol = lon.shape[1]

#when creating the df make the dtype as object to add list in it
test = pd.DataFrame(np.zeros([nrow,ncol])*np.nan, dtype = object);
for jj in range(ncol):
    for ii in range(nrow):
        print(ii, jj)
        test.iloc[ii, jj] = np.array([lonDat.iloc[ii, jj], latDat.iloc[ii, jj]])
        # test.iloc[ii, jj] = np.array([12.3543, 34.3453]).tolist()
        
test.to_csv('lonlatMesh.csv')