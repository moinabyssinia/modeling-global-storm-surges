# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:44:21 2021

combine extracted slp and wsp predictors 
create 100 csv files per tide gauge

@author: Michael Tadesse
"""
import os 
import pandas as pd

dir_in = "G:\\05_era5\\kikoStuff\\ensFiles\\02-eXtraction"
dir_out = "G:\\05_era5\\kikoStuff\\ensFiles\\03-combinedPredictors"


os.chdir(dir_in)
tgList = os.listdir()

#loop into each tide gauge

    #loop into each ensemble folder
    
        #load each predictor
        
            #rename columns
        
        #merge predictors
        
    #create a folder for each tide gauge
        
        #save each combined predictor 
        
        
def renameColumns(pred, colName):
    """
    renames dataframe columns
    """
    pred_col = list(pred.columns)
    for pp in range(len(pred_col)):
        if pred_col[pp] == 'date':
            continue
        pred_col[pp] = colName + str(pred_col[pp])
    pred.columns = pred_col
    

for tg in tgList:
    
    print(tg)
    
    #cd to tg folder
    os.chdir(tg)
    
    ensList = os.listdir()
    
    #loop through each ensemble
    for ens in ensList:
        
        print(ens)
        
        #cd to ens folder
        os.chdir(ens)
        
        #load predictors
        if (os.listdir()[0].endswith("SLP.csv")):
            print("slp found first")
            slp = pd.read_csv(os.listdir()[0])
            slp.drop('Unnamed: 0', axis = 1, inplace = True)
            #rename columns here
            renameColumns(slp, 'slp')
            
            wsp = pd.read_csv(os.listdir()[1])
            wsp.drop('Unnamed: 0', axis = 1, inplace = True)
            #rename columns here
            renameColumns(wsp, 'wsp')
            
        else:
            print("slp found second")
            slp = pd.read_csv(os.listdir()[1])  
            slp.drop('Unnamed: 0', axis = 1, inplace = True)
            #rename columns here
            renameColumns(slp, 'slp')
            
            wsp = pd.read_csv(os.listdir()[0]) 
            wsp.drop('Unnamed: 0', axis = 1, inplace = True)
            #rename columns here
            renameColumns(wsp, 'wsp')
            
