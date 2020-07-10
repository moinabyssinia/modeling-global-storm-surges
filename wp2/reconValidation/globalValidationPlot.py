# -*- coding: utf-8 -*-
"""
Created on Wed Jul 9 11:00:00 2020

To plot validations for reanalysis datasets

@author: Michael Tadesse
"""

def plotIt(reanalysis, metric):
    """
    this function organizes validation files
    and plots them

    reanalysis: {twcr, era20c, eraint, merra}
    metric: {corr, rmse}
    """
    #add libraries
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    #locate the file that basemap needs
    os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap"
    from mpl_toolkits.basemap import Basemap

    #dictionary for datasets
    data = {'twcr': ["20cr_Validation.csv", "20CR"],
            'era20c': ["era20c_Validation.csv", "ERA20C"],
            'eraint':["eraint_Validation.csv", "ERA-Interim"],
            'merra': ["merra_Validation.csv", "MERAA"]
            }
    
    metrics = {'corr': ["corrn_lr", "Pearson's Correlation"],
               'rmse': ["rmse_lr", "RMSE(m)"]
               }
    
    #cd to the validation directory
    os.chdir("D:\\data\\allReconstructions\\validation")
    
    #load validation files
    dat = pd.read_csv(data[reanalysis][0])
    
    #plotting
    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=10, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-80,urcrnrlat=80, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()
    m.bluemarble(alpha = 0.8) #basemap , alpha = transparency
    plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black', c = 
                dat[metrics[metric][0]], cmap = 'hot_r')
    m.colorbar(location = 'bottom')

    if metric == "corr":
        plt.clim(0, 1)
        
    title = data[reanalysis][1] + " - " + metrics[metric][1]
    plt.title(title)
    

def scoreAggregate(dat):
    """
    aggregates correlation and rmse
    scores of the reanalysis spatially
    """
    #set band column as nan to start
    dat['band'] = 'nan'
    
    for ii in range(0, len(dat)):
        if dat['lat'][ii] >= -90 and  dat['lat'][ii] <= -70:
            dat['band'][ii] = -80
        elif dat['lat'][ii] > -70 and  dat['lat'][ii] <= -50:
            dat['band'][ii] = -60
        elif dat['lat'][ii] > -50 and  dat['lat'][ii] <= -30:
            dat['band'][ii] = -40
        elif dat['lat'][ii] > -30 and  dat['lat'][ii] <= -10:
           dat['band'][ii] = -20
        elif dat['lat'][ii] > -10 and  dat['lat'][ii] <= 10:
            dat['band'][ii] = 0
        elif dat['lat'][ii] > 10 and  dat['lat'][ii] <= 30:
            dat['band'][ii] = 20
        elif dat['lat'][ii] > 30 and  dat['lat'][ii] <= 50:
            dat['band'][ii] = 40
        elif dat['lat'][ii] > 50 and  dat['lat'][ii] <= 70:
            dat['band'][ii] = 60
        elif dat['lat'][ii] > 70 and  dat['lat'][ii] <= 90:
            dat['band'][ii] = 80

    
    


