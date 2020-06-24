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