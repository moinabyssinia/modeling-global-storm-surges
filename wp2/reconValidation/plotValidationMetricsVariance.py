# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 09:47:48 2020

To plot variance of validation metrics

@author: Michael Tadesse
"""
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap


def plotMetricVariance(metric):
    """
    this function plots the variance of 
    the validation metrics for the reconstructed
    surges
    """
    
    #directories for the common period validation
    csvPath = "D:\\data\\allReconstructions\\validation\\commonPeriodValidation"
    os.chdir(csvPath)
    
    #define validation output files
    validationFiles = {'corr' : 'allCorr.csv', 'rmse' : 'allRMSE.csv',
                       'nse' : 'allNSE.csv'}
    
    chosenMetric = validationFiles[metric]
    
    #read the validation file of choice
    dat = pd.read_csv(chosenMetric)
    
    #compute standard deviation of metrics for all reanalysis
    metricColumns = dat[['20CR', 'ERA-20C', 'ERA-Interim', 'MERRA']]
    dat['metricStd'] = metricColumns.std(axis = 1, skipna = True)
    
    #plotting
    sns.set_context('notebook', font_scale = 1.5)
    
    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()
    
    #draw parallels and meridians 
    parallels = np.arange(-80,81,20.)
    m.drawparallels(parallels,labels=[True,False,False,False], linewidth = 0)
    
    #define bubble sizes
    minSize = min(dat['metricStd'])*5000
    maxSize = max(dat['metricStd'])*5000
    
    m.bluemarble(alpha = 0.8)
    sns.scatterplot(x = x, y = y, color = 'red', 
                    size = 'metricStd', hue = 'Reanalysis',
                    sizes = (minSize, maxSize), data = dat)