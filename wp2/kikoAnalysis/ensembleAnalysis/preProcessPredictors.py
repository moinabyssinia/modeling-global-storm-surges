# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:46:04 2021

pre-processsing predictor data 

@author: Michael Tadesse
"""
import os 
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

dir_in = "G:\\05_era5\\kikoStuff\\ensFiles\\03-combinedPredictors"
dir_numPC = "G:\\05_era5\\kikoStuff\\07-regCoef"
dir_out = "G:\\05_era5\\kikoStuff\\ensFiles\\04-dailyMeanSurge"


#get squared and cubed terms
os.chdir(dir_in)
tgList = os.listdir()

#loop through each tg
for tg in tgList:
    
    print(tg)
    os.chdir(dir_in + "\\" + tg)
    
    ensList = os.listdir()
    
    #loop through ensembles
    
    for ens in ensList:
        
        os.chdir(dir_in + "\\" + tg)
        
        dat  = pd.read_csv(ens)
        dat.drop('Unnamed: 0', axis = 1, inplace = True)
        
        #add squared and cubed wind terms (as in WPI model)
        pickTerms = lambda x: x.startswith('wsp')
        wndTerms = dat.columns[list(map(pickTerms, dat.columns))]
        wsp_sqr = dat[wndTerms]**2
        wsp_cbd = dat[wndTerms]**3
        dat = pd.concat([dat, wsp_sqr, wsp_cbd], axis = 1)

        #standardize predictor matrix
        datPred = dat.iloc[:,1:]
        scaler = StandardScaler()
        print(scaler.fit(datPred))
        dat_standardized = pd.DataFrame(scaler.transform(datPred), \
                                        columns = datPred.columns)
        dat_standardized = pd.concat([dat['date'], dat_standardized], \
                                      axis = 1)
        
        #get number of pcs
        os.chdir(dir_numPC)
        x = pd.read_csv(tg)
        numPC = len(x) - 1
        
        #apply pca
        #numPC = len(x)-1
        pca = PCA(numPC) #use the same number of PCs used for training
        pca.fit(dat_standardized.iloc[:,1:])
        datPC = pd.DataFrame(pca.transform(dat_standardized.iloc[:,1:]))
        
        #get daily mean surge
        xx = x['0'].tolist() #coefficients for pcs 
        
        datSurge = xx[0] + datPC.dot(xx[1:])
        datSurge = pd.concat([dat['date'], datSurge], axis = 1)
        saveName = ens.lower() + ".csv"
        
        #save as csv
        os.chdir(dir_out)
        
        #create tg folder
        try:
            os.makedirs(tg)
            os.chdir(tg)
            
            #save surge
            datSurge.to_csv(saveName)
        except FileExistsError:
           os.chdir(tg)
           
           #save ensemble combined predictors
           datSurge.to_csv(saveName)
        


