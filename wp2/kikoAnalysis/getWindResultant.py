# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:52:48 2020

@author: Michael Tadesse
"""


import os 
import pandas as pd

os.chdir()

uwnd = pd.read_csv('wnd_u.csv')
vwnd = pd.read_csv('wnd_v.csv')

#check sizes of uwnd and vwnd
if uwnd.shape == vwnd.shape:
    print("all good!")
else:
    print("sizes not equal")
    
uwnd.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)
vwnd.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)

#sort by date
uwnd = uwnd.sort_values(by = 'date')
vwnd = vwnd.sort_values(by = 'date')

#reset indices

#get squares of uwnd and vwnd
uSquare = uwnd.iloc[:, 1:]**2
vSquare = vwnd.iloc[:, 1:]**2

#sum and take square root
wndResultant = (uSquare + vSquare)**0.5
