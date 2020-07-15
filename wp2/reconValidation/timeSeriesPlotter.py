# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:22:00 2020

To plot reanalysis reconstruction timeseries

@author: Michael Tadesse
"""
#get libraries
import os 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def timeSeriesPlotter(tideGauge, data):
    """
    this function organizes five functions 
    to plot surge reconstruction
    """
    getFiles(tideGauge, data)


def getFiles(tideGauge, data):
    """
    this function gets the reconstruction time
    series and the observed surge time series

    tideGauge: name of the tide gauge with out .csv extension
    data = ["twcr", "era20c", "eraint", "merra"]
    """
    reconPath = {
        "twcr": "E:\\03_20cr\\08_20cr_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "era20c": "F:\\02_era20C\\08_era20C_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "eraint": "F:\\01_erainterim\\08_eraint_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "merra": "G:\\04_merra\\08_merra_surge_reconstruction\\bestReconstruction\\surgeReconstructed"
        }

    surgePath = "D:\\data\\allReconstructions\\05_dmax_surge_georef"

    tg = tideGauge+".csv"
    print(tg, '\n')

    surgeTwcr, surgeEra20c, surgeEraint, surgeMerra = [],[],[],[]
    #get reconstructed surge
    for ii in data:
        if ii == 'twcr':
            os.chdir(reconPath[ii])
            surgeTwcr = getReconSurge(tg)
        elif ii == 'era20c':
            os.chdir(reconPath[ii])
            surgeEra20c = getReconSurge(tg)
        elif ii == 'eraint':
            os.chdir(reconPath[ii])
            surgeEraint = getReconSurge(tg)
        elif ii == 'merra':
            os.chdir(reconPath[ii])
            surgeMerra = getReconSurge(tg)
        else:
            "there is a problem!"

    #get observed surge
    os.chdir(surgePath)
    obsSurge = getObsSurge(tg)

    #print(obsSurge)
    getTimeStamp(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, obsSurge)

def getReconSurge(tg):
    """
    to get the reconstruction surge 
    """
    #get reconstruction
    reconSurge = pd.read_csv(tg)
    ##remove duplicated rows
    reconSurge.drop(reconSurge[reconSurge['date'].duplicated()].index, axis = 0, inplace = True)
    reconSurge.reset_index(inplace = True)
    reconSurge.drop('index', axis = 1, inplace = True)

    return reconSurge

def getObsSurge(tg):
    """
    to get the observed surge
    """
    #get surge time series
    obsSurge = pd.read_csv(tg)
    ##remove duplicated rows
    obsSurge.drop(obsSurge[obsSurge['date'].duplicated()].index, axis = 0, inplace = True)
    obsSurge.reset_index(inplace = True)
    obsSurge.drop('index', axis = 1, inplace = True)

    return obsSurge

def getTimeStamp(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, obsSurge):
    """
    this function prepares the time column of the time series
    to make it easy to plot
    """

    #define lambda functions 
    time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    time_stamp_surge = lambda x: (datetime.strptime(x, '%Y-%m-%d'))

    if len(surgeTwcr) != 0:
        surgeTwcr['date'] = pd.DataFrame(list(map(time_stamp, surgeTwcr['date'])), columns = ['date'])
    if len(surgeEra20c) != 0:
        surgeEra20c['date'] = pd.DataFrame(list(map(time_stamp, surgeEra20c['date'])), columns = ['date'])
    if len(surgeEraint) != 0:
        surgeEraint['date'] = pd.DataFrame(list(map(time_stamp, surgeEraint['date'])), columns = ['date'])
    if len(surgeMerra) != 0 :
        surgeMerra['date'] = pd.DataFrame(list(map(time_stamp, surgeMerra['date'])), columns = ['date'])
    if len(obsSurge) != 0:
        obsSurge['date'] = pd.DataFrame(list(map(time_stamp_surge, obsSurge['ymd'])), columns = ['date'])
    
    #calling the plotter function
    plotTimeSeries(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, obsSurge)

def plotTimeSeries(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, obsSurge):
    """
    this function plots a time series making use of 
    all reconstructed surge data from reanalyses
    """
    plt.figure(figsize = (16,10))
    if len(obsSurge) != 0:
        plt.plot(obsSurge['date'], obsSurge['surge'], color = "blue", label = "observation")
    if len(surgeTwcr) != 0:
        plt.plot(surgeTwcr['date'], surgeTwcr['surge_reconsturcted'], color = "red", label = "twcr")
    if len(surgeEra20c) != 0:
        plt.plot(surgeEra20c['date'], surgeEra20c['surge_reconsturcted'], color = "green", label = "era20c")
    if len(surgeEraint) != 0:
        plt.plot(surgeEraint['date'], surgeEraint['surge_reconsturcted'], color = "black", label = "eraint")
    if len(surgeMerra) != 0:
        plt.plot(surgeMerra['date'], surgeMerra['surge_reconsturcted'], color = "cyan", label = "merra")
    
    plt.legend()