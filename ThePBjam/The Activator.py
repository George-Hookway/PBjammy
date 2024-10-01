# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:58:23 2024

@author: GTH025
"""

import pandas as pd
import PBjammer

Directory = 'C:/Users/GTH025/Documents/PBjammy'
BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')
exptime = 60
Mission='K2'
Plot = True
l1 = True
Type = 'SG'

for d in range(66, 67):
    if BigData.Teff[d] < 5400:
        print('Giant Star - moving on')
        continue
    print(BigData.iloc[d,])
    Result, f, s, M = PBjammer.Run(ID=f'EPIC{BigData.ID[d]}', numax=(BigData.numax[d], BigData.numax_e[d]),
                                dnu=(BigData.dnu[d], BigData.dnu_e[d]), teff=(BigData.Teff[d], BigData.Teff_e[d]),
                                bp_rp=(BigData.bp_rp[d], BigData.bp_rp_e[d]), exptime=exptime, Mission=Mission, Plot=Plot, l1=l1, Type=Type)

    FinalResult, Peak = PBjammer.PeakBagger(Result, f, s, Plot=Plot)

#%%

import pickle

OutputFileM = f'{Directory}/Output/Lightning McQueen/ModeID.pickle'
OutputFileP = f'{Directory}/Output/Lightning McQueen/Peakbagged.pickle'

with open(OutputFileP, 'wb') as file:
    pickle.dump(FinalResult, file)
