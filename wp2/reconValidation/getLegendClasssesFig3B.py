# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 10:50:35 2021

add a column of marker size - to create 
only four classes of legends with distinct
sizes - for correlation - to plot figure 3B

@author: Michael Tadesse
"""
import os
import pandas as pd

os.chdir("G:\\data\\allReconstructions\\validation"\
         "\\commonPeriodValidation")

#load corr/rmse/rrmse files
dat = pd.read_csv("allRMSEMetricVariance.csv")
dat.drop('Unnamed: 0', axis = 1, inplace = True)

#find the four classes - look at std histogram

##rmse - [1, 2, 4, 6]

dat['size'] = 'nan'

for ii in range(len(dat)):
    row = 100*dat['Metric Variance'][ii]**0.5 #in cms
    print(row)
    if (row <= 1.0):
        dat['size'][ii] = 50
    elif ((row > 1.0) & (row < 2.0)):
        dat['size'][ii] = 250
    elif ((row >= 2.0) & (row < 4.0)):
        dat['size'][ii] = 500
    elif ((row >= 4.0) & (row <= 6.0)):
        dat['size'][ii] = 750
    else:
        "something is wrong!"
        
#save as csv
dat.to_csv("rmseSTDFixedLegend.csv")