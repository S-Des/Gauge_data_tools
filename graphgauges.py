# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 16:37:13 2016

@author: simon.desmet
"""
# Import RAW rain and flow GAUGE data and then PLOT IT by TIME

import matplotlib.pyplot as plt

import pandas as pd

import pylab

import sys

import numpy as np

from datetime import datetime

# paste your paths here inside '' marks

# DAILY rain, add RAIN D,E,F etc if you whish
#RDALoc = r'C:\Shiremoor\North Tyneside RF\007864_BlagdonHall_DailyRF_011103_310715.csv'
#RDBLoc = r'C:\Shiremoor\North Tyneside RF\008332_Monkseaton_DailyRF_010905_310715.csv'
#RDCLoc = r''

# EA daily raingauge files have 21 lines of header material
#RDA_all = pd.read_csv(RDALoc, parse_dates=True, header=21)
#RDB_all = pd.read_csv(RDBLoc, parse_dates=True, header=21)
#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)


# 15minute rain, add RAIN D,E,F etc if you whish
R15ALoc = r'S:\Sheffield Based Jobs\CS082030_East_Riding_FRMPs\04 Shared\06 Authorities\EA\Gauge Data\20160216_15min_gaugedata\East Riding\TBR Data\041917_GREAT CULVERT LOGGER_RE.15.Total_240399_110216_CLEANED.csv'
#R15BLoc = r'C:\Shiremoor\North Tyneside RF\019356_JesmondDene_15minRF_010184_060316.csv'
#R15CLoc = r'C:\Shiremoor\North Tyneside RF\008632_WhitleyBay_15minRF_010507_060316.csv'

# EA 15 min raingauge files have 22 lines of header material
#R15A_all = pd.read_csv(R15ALoc, parse_dates='Date Time', header=20)
R15A_all = pd.read_csv(R15ALoc, parse_dates='Date Time', index_col='Date Time', header=20)

#R15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#R15A = R15A_all[['Date', 'RF_mm']]
R15A_all.columns = ['RF_mm','Quality','comments','A','B','C','D']
R15A = R15A_all[['RF_mm']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
R15A[['RF_mm']]=R15A[['RF_mm']].replace('.', '0')
R15A[['RF_mm']]=R15A[['RF_mm']].replace('---', '0')
R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)
fig=plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.plot(R15A)
ax1.set_xlim(01-01-2011,01-02-2011)


#R15A['RF_mm'].ix['01-2011':'03-2011'].plot()
#ax2 = fig.add_subplot(2,2,2)
#ax2.plot(R15A['RF_mm'].ix['01-2011':'03-2011'])
#ax3 = fig.add_subplot(2,2,3)
#ax3.plot(R15A['RF_mm'].ix['01-01-2011':'01-10-2011'])