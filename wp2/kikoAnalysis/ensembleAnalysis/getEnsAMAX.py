# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:45:38 2021

get AMAX from daily mean surge - from the 100 ensemble surges

@author: Michael Tadesse
"""
#import packages
import os
import pandas as pd

#define directories
dir_in = 'G:\\05_era5\\kikoStuff\\ensFiles\\04-dailyMeanSurge'
csv_path = 'G:\\05_era5\\kikoStuff\\ensFiles\\05-ensAMAX'
amax_path = "G:\\05_era5\\kikoStuff\\aMaxEurope\\annualMax"

#load files first
os.chdir(dir_in)

#looping through tgs
for tg in os.listdir():
    #read individual csv files
    print(tg)
    os.chdir(dir_in + "\\" + tg)
    
    #loop through ensemble files
    ensList = os.listdir()
    
    for ens in ensList:
        
        os.chdir(dir_in + "\\" + tg) 
        dat = pd.read_csv(ens)    
        dat.drop('Unnamed: 0', axis = 1, inplace = True)
        dat.columns = ['date', 'surge']
        
        #get the year part
        getYear = lambda x: x.split('-')[0]
        dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

        #looping thorough the years to extract amax
        firstTry = True
        for yr in dat['year'].unique():
            print(yr)
            
            currentYearData = dat[dat['year'] == yr]
            currentAmax =  currentYearData['surge'].max()
            
            #find the row where amax is located
            amax = currentYearData[currentYearData['surge'] == currentAmax]
            
            #reorder columns
            amax = amax.reindex(['year', 'surge'], axis = 1)
            
            if firstTry:
                annualMax = amax
                firstTry = False
        
            else:
                annualMax = pd.concat([annualMax, amax], axis = 0, sort= False)
            
            annualMax.reset_index(inplace = True)
            annualMax.drop(['index'], axis = 1, inplace = True)
            
            #get lon/lat
            os.chdir(amax_path)
            x = pd.read_csv(tg)
            annualMax['lon'] = x['lon'][0]
            annualMax['lat'] = x['lat'][0]
            
            saveName = ens.split('.csv')[0] + "Amax.csv"
            tgName = tg.split('.csv')[0]
        #save as csv
        os.chdir(csv_path)
        
        #create tg folder
        try:
            os.makedirs(tgName)
            os.chdir(tgName)
            
            #save surge
            annualMax.to_csv(saveName)
        except FileExistsError:
           os.chdir(tgName)
           
           #save ensemble combined predictors
           annualMax.to_csv(saveName)
        
            
    
        
        
        
        
        