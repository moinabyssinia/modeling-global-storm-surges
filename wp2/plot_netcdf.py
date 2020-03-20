# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:30:46 2020
Plotting NetCDF files 
@author: Michael Tadesse
"""

#load netcdf file
prs = Dataset('era_interim_slp_1987_1990.nc')
slp = prs.variables['msl'][:]

#subset a portiong of the array to plot it
slp_test = slp[4385,:,:]

#flip it to correctly plot
slp_test_flip = slp[::-1]

#plot
plt.figure()
v_map = plt.contourf(vwnd_test, cmap = 'hot_r')
plt.colorbar()

