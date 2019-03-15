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
F15ALoc = r'S:\Sheffield Based Jobs\CS082030_East_Riding_FRMPs\04 Shared\06 Authorities\EA\Gauge Data\20151105_EA_Rain_data\Files\Flow & Level Sites\L3341_Winestead Booster_HD.15.P_110803_180215_mod.csv'
G1Title = 'Winestead_Booster'
F15BLoc = r'C:\East_Riding_FRMP\calibration_workingfolder\L3350_Skeffling PS_SG.15.P_110803_170215.csv'
G2Title = 'Skeffling_Pumpstation'
F15CLoc = r'C:\East_Riding_FRMP\calibration_workingfolder\L3316_Burstwick Hall Road Bridge_SG.15.P_110803_110215.csv'
G3Title = 'Burstwick_Hall_Road'
F15DLoc = r'C:\East_Riding_FRMP\calibration_workingfolder\L3330_Thorngumbald_SG.15.P_090303_170215.csv'
G4Title = 'Thorngumbald'
F15ELoc = r'C:\East_Riding_FRMP\calibration_workingfolder\L3335_Keyingham Road Bridge_SG.15.P_010403_160215.csv'
G5Title = 'Keyingham_Road'
F15FLoc = r'C:\East_Riding_FRMP\calibration_workingfolder\L3314_Hedon Westlands Drain_Upstream.15.P_130706_160215.csv'
G6Title = 'Hedon_Westlands'
#F15GLoc = r'C:\East_Riding_FRMP\calibration_workingfolder\L3314_Hedon Westlands Drain_Upstream.15.P_130706_160215.csv'
#G7Title = 'Hedon_Westlands'

fig=plt.figure()

#F15ELoc = r''
# EA 15 min raingauge files have 22 lines of header material
#F15A_all = pd.read_csv(F15ALoc, parse_dates='Date Time', header=20)


#==== Graph A
#F15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15A = R15A_all[['Date', 'RF_mm']]
F15A_all = pd.read_csv(F15ALoc, parse_dates='Date Time', index_col='Date Time', header=20)
F15A_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C','D']
F15A = F15A_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
F15A[['Stage_m']]=F15A[['Stage_m']].replace('.', '0')
F15A[['Stage_m']]=F15A[['Stage_m']].replace('---', '0')
F15A[['Stage_m']]=F15A[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)

ax1 = fig.add_subplot(6,1,1)
ax1.plot(F15A['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
ax1.set_title(G1Title)
#plt.xticks(rotation=90)
#ax1.set_xlim(01-01-2011,01-02-2011)



#==== Graph B
F15B_all = pd.read_csv(F15BLoc, parse_dates='Date Time', index_col='Date Time', header=20)
#F15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15A = R15A_all[['Date', 'RF_mm']]
F15B_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C']
F15B = F15B_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
F15B[['Stage_m']]=F15B[['Stage_m']].replace('.', '0')
F15B[['Stage_m']]=F15B[['Stage_m']].replace('---', '0')
F15B[['Stage_m']]=F15B[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)

ax2 = fig.add_subplot(6,1,2)
ax2.plot(F15B['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
ax2.set_title(G2Title)
#plt.xticks(rotation=90)
#ax1.set_xlim(01-01-2011,01-02-2011)


#==== Graph C
F15C_all = pd.read_csv(F15CLoc, parse_dates='Date Time', index_col='Date Time', header=20,)
#F15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15A = R15A_all[['Date', 'RF_mm']]
F15C_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C','D']
F15C = F15C_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
F15C[['Stage_m']]=F15C[['Stage_m']].replace('.', '0')
F15C[['Stage_m']]=F15C[['Stage_m']].replace('---', '0')
F15C[['Stage_m']]=F15C[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)

ax3 = fig.add_subplot(6,1,3)
ax3.plot(F15C['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
ax3.set_title(G2Title)


#==== Graph D
F15D_all = pd.read_csv(F15DLoc, parse_dates='Date Time', index_col='Date Time', header=20)
#F15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15A = R15A_all[['Date', 'RF_mm']]
F15D_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C','D']
F15D = F15D_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
F15D[['Stage_m']]=F15D[['Stage_m']].replace('.', '0')
F15D[['Stage_m']]=F15D[['Stage_m']].replace('---', '0')
F15D[['Stage_m']]=F15D[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)

ax4 = fig.add_subplot(6,1,4)
ax4.plot(F15D['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
ax4.set_title(G4Title)


#==== Graph E
F15E_all = pd.read_csv(F15ELoc, parse_dates='Date Time', index_col='Date Time', header=20)
#F15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15A = R15A_all[['Date', 'RF_mm']]
F15E_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C','D']
F15E = F15E_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
F15E[['Stage_m']]=F15E[['Stage_m']].replace('.', '0')
F15E[['Stage_m']]=F15E[['Stage_m']].replace('---', '0')
F15E[['Stage_m']]=F15E[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)
ax5 = fig.add_subplot(6,1,5)
ax5.plot(F15E['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
ax5.set_title(G5Title)


#==== Graph F
F15F_all = pd.read_csv(F15FLoc, parse_dates='Date Time', index_col='Date Time', header=20)
#F15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15A = R15A_all[['Date', 'RF_mm']]
F15F_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C','D']
F15F = F15F_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
F15F[['Stage_m']]=F15F[['Stage_m']].replace('.', '0')
F15F[['Stage_m']]=F15F[['Stage_m']].replace('---', '0')
F15F[['Stage_m']]=F15F[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)

ax6 = fig.add_subplot(6,1,6)
ax6.plot(F15F['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
ax6.set_title(G6Title)


fig.subplots_adjust(hspace=1)


#==== Graph G
#F15G_all = pd.read_csv(F15GLoc, parse_dates='Date Time', index_col='Date Time', header=20)
#F15A_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15A = R15A_all[['Date', 'RF_mm']]
#F15G_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C','D']
#F15G_all=F15G_all.rename(columns())
#F15G = F15G_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
#F15G[['Stage_m']]=F15G[['Stage_m']].replace('.', '0')
#F15G[['Stage_m']]=F15G[['Stage_m']].replace('---', '0')
#F15G[['Stage_m']]=F15G[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)

#ax7 = fig.add_subplot(7,1,7)
#ax7.plot(F15G['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
#ax7.set_title(G7Title)



#==== Graph H
#F15H_all = pd.read_csv(F15BLoc, parse_dates='Date Time', index_col='Date Time', header=20)
#F15H_all.columns = ['Date','RF_mm','Quality','comments','A','B','C','D']
#F15H = R15H_all[['Date', 'RF_mm']]
#F15H_all.columns = ['Stage_m','stage_b','Quality','Comments','B','C','D']
#F15H = F15H_all[['Stage_m']]

#pd.to_numeric(R15A[['RF_mm']], errors='coerce')
#F15H[['Stage_m']]=F15H[['Stage_m']].replace('.', '0')
#F15H[['Stage_m']]=F15H[['Stage_m']].replace('---', '0')
#F15H[['Stage_m']]=F15H[['Stage_m']].astype(float)
#R15A[['Date']] = R15A[['Date']].to_datetime('Date', format;'%Y%m%d)
#R15A[['RF_mm']] = R15A[['RF_mm']].astype(float)
#R15B_all = pd.read_csv(RDBLoc, parse_dates=True, header=20)

#RDC = pd.read_csv(RDCLoc, parse_dates=True, header=21)
#fig=plt.figure()
#ax8 = fig.add_subplot(7,1,8)
#ax8.plot(F15H['Stage_m'].ix['25-06-2007 01:00:00':'29-06-2007 01:00:00'])
#ax8.set_title(G8Title)



#R15A['RF_mm'].ix['01-2011':'03-2011'].plot()
#ax2 = fig.add_subplot(2,2,2)
#ax2.plot(R15A['RF_mm'].ix['01-2011':'03-2011'])
#ax3 = fig.add_subplot(2,2,3)
#ax3.plot(R15A['RF_mm'].ix['01-01-2011':'01-10-2011'])