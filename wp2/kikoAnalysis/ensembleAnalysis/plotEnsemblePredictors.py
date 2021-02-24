# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:05:59 2021

plot ensemble data

@author: Michael Tadesse
"""

#setup the basemap

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
          urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, \
              resolution='c')
x,y = lon, lat
m.drawcoastlines()

#use pcolor to ovelay the map

plt.pcolormesh(lon, lat, test)