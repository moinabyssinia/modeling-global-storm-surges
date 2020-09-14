# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:53:27 2020

Figure 1c and 1d 

@author: Michael Tadesse
"""

#get the grid_stat file from 
##"F:\01_erainterim\06_eraint_results\grid_size"

plt.figure(figsize = (10,6))
markers = {"10x10": "o", "8x8": "o", "6x6":'o', "4x4":'o', "3x3":'o', "2x2":'o', "1x1":'o'}
sns.scatterplot('time', 'avg_corr', style = 'grid_size', s = 100, hue = 'grid_size', data = dat)
plt.grid(alpha = 0.5)
plt.ylabel('Average Correlation')
plt.xlabel('Run-time (hrs.)')

os.chdir("G:\\data\\manuscriptFiles\\figures")
plt.savefig('figure1c.svg', dpi = 400)


#figure 1d
plt.figure(figsize = (10,6))
markers = {"10x10": "o", "8x8": "o", "6x6":'o', "4x4":'o', "3x3":'o', "2x2":'o', "1x1":'o'}
sns.scatterplot('time', dat['avg_rmse']*100, style = 'grid_size', s = 100, hue = 'grid_size', data = dat)
plt.grid(alpha = 0.5)
plt.ylabel('Average RMSE (cm)')
plt.xlabel('Run-time (hrs.)')

os.chdir("G:\\data\\manuscriptFiles\\figures")
plt.savefig('figure1d.svg', dpi = 400)