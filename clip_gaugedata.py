# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 10:55:31 2016

@author: simon.desmet
"""
#Import Flow Guage data and trim to specified dates

import pandas as pd

#import sys

#from datetime import datetime


gaugedata = r'C:\East_Riding_FRMP\Calibration_Gauge_Data\Nov11\F2807_Buttercrambe_FQH.ir_030973_180215.csv'

gaugename ='Buttercramb_FQ'
#the name of your gauge
saveloc = r'C:\East_Riding_FRMP\Calibration_Gauge_Data\Crambe'
# path to your raw EA gauge data file


alldata = pd.read_csv(gaugedata, parse_dates='Date Time', index_col='Date Time', header=20)

# use Pandas to read in the csv and parse dates to date time, 
#default header is 20 but this may need adjusting to 19 or 21 depending on file

#gaugetype = 'Flow'

# relabel the gauge type depending on your gauge, it could be head, stage or flow.

#alldata.columns = [gaugetype,'X_AOD','Quality']

#rename all columns, sometimes extra dummy columns must be added due to use of commas in comments

# set your start and end to times you want to clip.
start = '01-01-2011 00:00:00'

end = '01-01-2014 00:00:00'

clipdata=alldata[start:end]
#cuts our data down to just the dates we want

print clipdata

startdate = start[0:10]
clipdata.to_csv(saveloc+str(startdate)+str(gaugename)+'.csv')

#F15F = F15F_all[['Stage_m']]





