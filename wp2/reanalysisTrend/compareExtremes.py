# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:43:56 2020

compare the extremes in observed and reconstructed
surges for a longer period of time

@author: Michael Tadesse
"""
import os 
import pandas as pd


def getExtremes(timeSeries, percentile):
    """
    this function gets the extremes in the 
    observation and their corresponding
    reconstructed values
    """
    
    

def loadTimesSeries(tideGauge, reanalysis):
    """
    this function loads a time series
    for the chosen tide gauge
    
    tideGauge = ['victoria', 'fremantle', 'brest', 'atlanticCity']
    reanalysis = ['Twcr', 'Era20c']
    """
    os.chdir("G:\\data\\reanalysisTrendFiles\\reconSurgeFiles")
    dat = pd.read_csv(tideGauge+reanalysis+"Merged.csv")
    dat.drop(['Unnamed: 0', 'index', 'Unnamed: 0.1'], axis = 1, inplace = True)
    return dat