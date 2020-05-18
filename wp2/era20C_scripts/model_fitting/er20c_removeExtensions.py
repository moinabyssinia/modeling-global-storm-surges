# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:39:37 2020

This program removes the filename extensions 
from surge reconstruction files

@author: Michael Tadesse
"""

def removeExtension():
    """
    removes file extensions
    """
    
    import os
    import pandas as pd
    
    
    
    dir_in = 'F:\\02_era20C\\08_era20C_surge_reconstruction\\bestReconstruction\\surgeReconstructed'
    dir_out = 'F:\\02_era20C\\08_era20C_surge_reconstruction\\bestReconstruction\\surgeReconstructed_new'


    os.chdir(dir_in)
    
    tg_list = os.listdir()
    extenstion = ['-glossdm-bodc', '-uhslc', '-jma', '-bodc', '-noaa',\
                  '-med-refmar', '-pde', '-meds', '-noc', '-ieo', '-idromare',\
                      '-eseas', 'france-refmar', '-noc', '-smhi', '-bsh',\
                          '-fmi', '-rws', '-dmi', '-statkart', '-coastguard',\
                              '-itt', '-comune_venezia', '-johnhunter', '-university_zagreb']
    for ii in tg_list:
        
    
    
    
    
