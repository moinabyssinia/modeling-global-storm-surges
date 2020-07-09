# -*- coding: utf-8 -*-
"""
Created on Wed Jul 9 11:00:00 2020

To plot validations for reanalysis datasets

@author: Michael Tadesse
"""

def plotIt(reanalysis):
    """
    this function organizes validation files
    and plots them

    data: {twcr, era20c, eraint, merra}
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
    
    #cd to the validation directory
    os.chdir("D:\\data\\allReconstructions\\validation")
    
    #load validation files
    dat = pd.read_csv(data[reanalysis][0])
    
    #plotting
    fig=plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=10, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-80,urcrnrlat=80, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()
    m.bluemarble(alpha = 0.8) #basemap , alpha = transparency
    plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black', c = dat['corrn_lr'], cmap = 'hot_r')
    cbar = m.colorbar(location = 'bottom')
    plt.clim(0, 1)
    plt.title(data[reanalysis][1])

