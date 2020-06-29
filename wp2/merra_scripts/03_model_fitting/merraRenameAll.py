# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:45:47 2020

@author: WahlInstall
"""
import os

def renameFiles():
    for tg in os.listdir():
        charToRemove = ",-"
        
        for ii in charToRemove:
            newName = tg.replace(ii, "_")
        #now rename folder
        os.rename(tg, newName)
    print("it is finished!")
    
###########################################
#rename metadata csvs
###########################################
    
dir_in = os.chdir("E:\\03_20cr\\08_20cr_surge_reconstruction\\bestReconstruction\\metaData")
dat = pd.read_csv("20cr_modelValidationKFOLD.csv")

def renameMetaData():
    for ii in range(0, len(dat)):
        oldName = dat['tg'][ii]
        charToRemove = ",-"
        
        for jj in charToRemove:
            newName= oldName.replace(jj, "_")
        print(oldName, " ", newName)
        dat.iloc[ii, 1] = newName
        

renameMetaData()

dat.drop('Unnamed: 0', axis = 1, inplace = True)

dat.to_csv('20cr_Validation.csv')
