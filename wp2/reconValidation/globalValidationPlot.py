# -*- coding: utf-8 -*-
"""
Created on Wed Jul 9 11:00:00 2020

To plot validations for reanalysis datasets

@author: Michael Tadesse
"""

def plotIt():
    """
    this function organizes validation files
    and plots them

    data: {twcr, era20c, eraint, merra}
    """
    #add libraries
    import os
    import pandas as pd
    import matplotlib.pyplot as plot
    #locate the file that basemap needs
    os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap"
    from mpl_toolkits.basemap import Basemap

    #load



#run function
plotIt()