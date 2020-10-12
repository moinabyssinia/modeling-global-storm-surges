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



import matplotlib.pyplot as plt
import seaborn as sns


leftPane = pd.read_csv('figure5leftpane.csv')
rightPane = pd.read_csv('figure5rightpane.csv')

fig, axes = plt.subplots(3, 2, figsize=(16, 10))
palette = {"20CR":"green", "ERA-20C":"magenta", "ERA-Interim":"black", 
           "MERRA":"red", "ERA5":"cyan"}
sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[0,0])
axes[0,0].legend()

sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[0,1])

sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[1,0])

sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[1,1])

sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[2,0])

sns.barplot(x = 'region', y ='corr', hue = 'reanalysis', data = leftPane, 
            palette = palette, ax = axes[2,1])