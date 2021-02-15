# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 09:47:48 2020
edited on Tuw Feb 09 10:37:00 2021

To plot STD of validation metrics
with constant legend circles size

@author: Michael Tadesse
"""
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap


def plotExtremeMetricVariance(metric):
    """
    this function plots the variance of 
    the validation metrics for the reconstructed
    surges
    """
    
    #directories for the common period validation
    csvPath = "G:\\data\\allReconstructions\\validation\\"\
                        "commonPeriodValidationExtremes\\percentile"
    os.chdir(csvPath)
    
    #define validation output files
    validationFiles = {'corr' : 'corrSTDFixedLegend.csv', 
                       'rmse' : 'rmseSTDFixedLegend.csv',
                       'nnse' : 'allNSEMetricVariance_v2.csv',
                       'rrmse':'rrmseSTDFixedLegend.csv'}
    
    chosenMetric = validationFiles[metric]
    
    #read the validation file of choice
    dat = pd.read_csv(chosenMetric)
    
    #remove nans
    dat = dat[dat['size'] != 'nan']
    dat = dat[~dat['size'].isna()]


    #plotting titles
    if metric == 'corr':
        title = 'Pearson\'s Correlation - Variation of Model Accuracy among Reanalyses'
    elif metric == 'rmse':

        title = 'RMSE - Metric Variation of Model Accuracy among Reanalyses (cm)'
    elif metric == 'rrmse':
        title = 'RRMSE - Metric Variation of Model Accuracy among Reanalyses (cm)'
    else:
        title = 'NNSE - Variation of Model Accuracy among Reanalyses'
        
    sns.set_context('notebook', font_scale = 1.5)
    
    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, \
                  resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()
    
    #draw parallels and meridians 
    parallels = np.arange(-80,81,20.)
    m.drawparallels(parallels,labels=[True,False,False,False], \
                    linewidth = 0)
    
    
    m.bluemarble(alpha = 0.8)
    sns.scatterplot(x = x, y = y, color = 'red', 
                    size = 'size', sizes = (30, 300),
                        hue = 'Reanalysis',
                        palette = {'ERA-Interim':'black', 
                                   'ERA-FIVE':'cyan', 
                                   'MERRA':'red', 
                                   'ERA-20C':'magenta', 
                                   '20CR':'green'}
                    ,data = dat)
    plt.title(title)
    
    plt.legend(ncol = 7)
    
    #saving as csv
    os.chdir("G:\\data\\allReconstructions\\validation\\"\
                 "commonPeriodValidationExtremes\\percentile\\plotFiles")
    saveName = 'allReanalyses'+metric+'STDFixedLegend.svg'
    plt.savefig(saveName, dpi = 400)