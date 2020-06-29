# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:45:47 2020

@author: WahlInstall
"""
import os

###########################################
#rename files or folders
###########################################
def renameFiles():
    for tg in os.listdir():
        charToRemove = ",-"
        
        for ii in charToRemove:
            newName = tg.replace(ii, "_")
        #now rename folder
        os.rename(tg, newName)
    print("it is finished!")
    
###################################################
#rename metadata csvs - when editing inside the csv 
###################################################
    
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


###################################################
#remove extensions within csv files + add path
###################################################


extenstion = ['_glossdm_bodc', '_uhslc', '_jma', '_bodc', '_noaa',\
              '_med_refmar', '_pde', '_meds', '_noc', '_ieo', '_idromare',\
                  '_eseas', 'france_refmar', '_noc', '_smhi', '_bsh',\
                      '_fmi', '_rws', '_dmi', '_statkart', '_coastguard',\
                          '_itt', '_comune_venezia', '_johnhunter', '_university_zagreb']

dat = twcr.copy()    

for ii in range(0, len(dat)):
    
    for ext in extenstion:

        if dat['tg'][ii].endswith(ext+".csv"):
            print(dat['tg'][ii],"----ENDS WITH---- [", ext, "]")
                                
            #split it
            new_name = dat['tg'][ii].split(ext+'.csv')[0] + str(".csv")
            
            #rename file
            dat.iloc[ii, 1] = new_name
            break
dat.drop('Unnamed: 0', axis = 1, inplace = True)

dat.to_csv('twcrMetadata.csv')
            