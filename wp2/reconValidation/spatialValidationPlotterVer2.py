# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:00:00 2020

where does each Reanalysis perform best
spatially?

Added NSE metric

@author: Michael Tadesse
"""
import os 
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap

def starter():
    #load the files
    twcrDat, era20cDat, eraintDat, merraDat = loadData()
    #get metrics for all reanalysis concatented by column
    allCorr = processData(twcrDat, era20cDat, eraintDat, merraDat)[0]
    allRMSE = processData(twcrDat, era20cDat, eraintDat, merraDat)[1]
    allNSE = processData(twcrDat, era20cDat, eraintDat, merraDat)[2]

    return allCorr, allRMSE, allNSE

def plotGlobal(metric):
    """
    this function plots the chosen metric 
    globallly using the basemap library

    metric = {'corr', 'rmse', 'nse'}

    """
    #set plotting details for each metric
    if metric == 'corr':
        dat = starter()[0]
        varToPlot = 'Correlation'
        title = 'Pearson\'s Correlation - 1980-2010'
        bubbleSizeMultiplier = 200
    elif metric == 'nse':
        dat = starter()[2]
        varToPlot = 'NSE(%)'
        title = 'NSE(%) - 1980-2010'  
        bubbleSizeMultiplier = 3
    else:
        dat = starter()[1]
        varToPlot = 'RMSE(cm)'
        title = 'RMSE(cm) - 1980-2010'
        bubbleSizeMultiplier = 10

    #increase plot font size
    sns.set_context('notebook', font_scale = 1.5)
    
    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()

    #get degree signs 
    parallels = np.arange(-80,81,20.)
    m.drawparallels(parallels,labels=[True,False,False,False], linewidth = 0)

    m.bluemarble(alpha = 0.8) 
    
    #define markers -use same for all for now
    markers = {"20CR": "o", "ERA-20C": "o", "ERA-Interim":'o', "MERRA":'o'}
    #define palette
    color_dict = dict({'20CR':'green',
                  'ERA-20C':'magenta',
                  'ERA-Interim': 'black',
                  'MERRA': 'red'
                  })
    #define bubble sizes
    minSize = min(dat[varToPlot])*bubbleSizeMultiplier
    maxSize = max(dat[varToPlot])*bubbleSizeMultiplier
    
    sns.scatterplot(x = x, y = y, markers = markers, style = 'Reanalysis',\
                    size = varToPlot, sizes=(minSize, maxSize),\
                        hue = 'Reanalysis',  palette = color_dict, data = dat)
    plt.legend(loc = 'lower left')
    plt.title(title)

def processData(twcrDat, era20cDat, eraintDat, merraDat):
    """
    this function cleans and prepares
    the data for plotting
    """
    #merge everything
    twcr_era20c = pd.merge(twcrDat, era20cDat, on='tg', how='left')
    twcr_era20c_eraint = pd.merge(twcr_era20c, eraintDat, on='tg', how='left')
    twcr_era20c_eraint_merra = pd.merge(twcr_era20c_eraint, merraDat, on='tg', 
                                        how='left')
    
    allCorr = twcr_era20c_eraint_merra[['tg', 'lon', 'lat', 'corrTwcr', 
    'corrEra20c', 'corrEraint', 'corrMerra']]
    allCorr.columns = ['tg', 'lon', 'lat', '20CR', 'ERA-20C', 'ERA-Interim', 
                       'MERRA']
    allRMSE = twcr_era20c_eraint_merra[['tg', 'lon', 'lat',  'rmseTwcr', 
                                        'rmseEra20c','rmseEraint',  'rmseMerra']]
    allRMSE.columns = ['tg', 'lon', 'lat', '20CR', 'ERA-20C', 'ERA-Interim', 'MERRA']
    allNSE = twcr_era20c_eraint_merra[['tg', 'lon', 'lat',  'nseTwcr', 
                                       'nseEra20c','nseEraint',  'nseMerra']]
    allNSE.columns = ['tg', 'lon', 'lat', '20CR', 'ERA-20C', 'ERA-Interim', 
                      'MERRA']
    
    #get max corr values 
    allCorr['Correlation'] = allCorr.iloc[:,3:7].max(axis = 1)
    allCorr['Reanalysis'] = allCorr.iloc[:, 3:7].idxmax(axis = 1)

    #get min rmse values - change to cms for visibility
    allRMSE['RMSE(cm)'] = allRMSE.iloc[:,3:7].min(axis = 1)*100
    allRMSE['Reanalysis'] = allRMSE.iloc[:, 3:7].idxmin(axis = 1)

    #get max nse values 
    allNSE['NSE(%)'] = allNSE.iloc[:,3:7].max(axis = 1)*100
    allNSE['Reanalysis'] = allNSE.iloc[:, 3:7].idxmax(axis = 1)
    
    # #save metrics results 
    # allCorr.to_csv("allCorr.csv")
    # allRMSE.to_csv("allRMSE.csv")
    # allNSE.to_csv("allNSE.csv")
    
    return allCorr, allRMSE, allNSE

def loadData():
    """
    loads the relevant validation files
    """
    #dictionary for datasets
    data = {'twcr': ["twcr19802010Validation.csv", "20CR"],
            'era20c': ["era20c19802010Validation.csv", "ERA20C"],
            'eraint':["eraint19802010Validation.csv", "ERA-Interim"],
            'merra': ["merra19802010Validation.csv", "MERAA"]
            }
    os.chdir("D:\\data\\allReconstructions\\validation\\commonPeriodValidation")

    twcrDat = pd.read_csv(data['twcr'][0])
    twcrDat.columns = ['deleteIt','tg', 'lon', 'lat', 'reanalysis', 
                       'corrTwcr', 'rmseTwcr', 'nseTwcr']
    era20cDat = pd.read_csv(data['era20c'][0])
    era20cDat.columns = ['deleteIt','tg', 'long', 'latt', 'reanalysis', 
                         'corrEra20c', 'rmseEra20c', 'nseEra20c']
    eraintDat = pd.read_csv(data['eraint'][0])
    eraintDat.columns = ['deleteIt','tg', 'long', 'latt', 'reanalysis', 
                         'corrEraint', 'rmseEraint', 'nseEraint']
    merraDat = pd.read_csv(data['merra'][0])
    merraDat.columns = ['deleteIt','tg', 'long', 'latt', 'reanalysis', 
                        'corrMerra', 'rmseMerra', 'nseMerra']


    return twcrDat, era20cDat, eraintDat, merraDat
