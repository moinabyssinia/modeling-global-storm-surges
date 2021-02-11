# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 10:50:35 2021

add a column of marker size - to create 
only four classes of legends with distinct
sizes

@author: Michael Tadesse
"""
import os

os.chdir("G:\\data\\allReconstructions\\validation"\
         "\\commonPeriodValidation")

#load corr/rmse/rrmse files
dat = pd.read_csv("allCorrelationMetricVariance.csv")
dat.drop('Unnamed: 0', axis = 1, inplace = True)

#find the four classes - look at std histogram

##correlation - [0.1, 0.2, 0.3, 0.5]

dat['size'] = 'nan'

for ii in range(len(dat)):
    row = dat['Metric Variance'][ii]**0.5
    print(row)
    if (row <= 0.1):
        dat['size'][ii] = 30
    elif ((row > 0.1) & (row < 0.2)):
        dat['size'][ii] = 50
    elif ((row >= 0.2) & (row < 0.3)):
        dat['size'][ii] = 90
    elif ((row >= 0.3) & (row <= 0.6)):
        dat['size'][ii] = 170
    else:
        "something is wrong!"
        
#save as csv
dat.to_csv("corrSTDFixedLegend.csv")