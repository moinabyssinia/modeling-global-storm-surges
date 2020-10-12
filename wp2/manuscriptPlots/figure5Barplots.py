# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:16:32 2020

This script plots figure 5 - the barplot
for the the corr rmse and nse 


@author: Michael Tadesse
"""

#first load the two time series
#total time series and extreme time series
#folder  == G:\data\manuscriptFiles\csvs


import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


leftPane = pd.read_csv('figure5leftpane.csv')
rightPane = pd.read_csv('figure5rightpane.csv')

fig, axes = plt.subplots(3, 2, figsize=(16, 10))
#spacing between subplots
fig.tight_layout(pad=1.0)
palette = {"20CR":"green", "ERA-20C":"magenta", "ERA-Interim":"black", 
           "MERRA":"red", "ERA5":"cyan"}
#correlation
sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[0,0])
axes[0,0].legend(ncol = 6)

#rmse
sns.barplot(x = 'region', y ='rmse', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[1,0])
axes[1,0].get_legend().set_visible(False)

#nnse
sns.barplot(x = 'region', y ='nnse', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[2,0])
axes[2,0].get_legend().set_visible(False)


#extremes - right pane

#correlation
sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = rightPane, 
            palette = palette, ax = axes[0,1])
axes[0,1].get_legend().set_visible(False)

#rmse
sns.barplot(x = 'region', y ='rmse', hue = 'reanalysis', data = rightPane, 
            palette = palette, ax = axes[1,1])
axes[1,1].get_legend().set_visible(False)

#nnse
sns.barplot(x = 'region', y ='nnse', hue = 'reanalysis', data = rightPane, 
            palette = palette, ax = axes[2,1])
axes[2,1].get_legend().set_visible(False)

#save as svg
os.chdir("G:\\data\\manuscriptFiles\\figures")