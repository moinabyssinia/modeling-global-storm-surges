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
        "twcr": "E:\\03_20cr\\08_20cr_surge_reconstruction\\\
            bestReconstruction\\surgeReconstructed",
        "era20c": "F:\\02_era20C\\08_era20C_surge_reconstruction\\\
            bestReconstruction\\surgeReconstructed",
        "eraint": "F:\\01_erainterim\\08_eraint_surge_reconstruction\\\
            bestReconstruction\\surgeReconstructed",
        "merra": "G:\\04_merra\\08_merra_surge_reconstruction\\bestReconstruction\\\
            surgeReconstructed"
        }

    surgePath = "D:\\data\\allReconstructions\\05_dmax_surge_georef"

    #print(reconPath[data])

    