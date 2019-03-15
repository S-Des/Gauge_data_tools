# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:07:40 2016

@author: simon.desmet
"""

import matplotlib.pyplot as plt
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
import pandas as pd

GRPH1loc= r'C:\D\ot20-06-2007Burstwick_Hall_Road.csv'
GRPH1T='Burstwick_Hall_Road'

Level1 = pd.read_csv(GRPH1loc, parse_dates='Date Time', index_col='Date Time')

print Level1











fig=plt.figure(figsize=(12,8), dpi=100, facecolor='w', edgecolor='w')

ax1 = fig.add_subplot(6,1,1)
ax1.plot(Level1)
ax1.set_title(GRPH1T)