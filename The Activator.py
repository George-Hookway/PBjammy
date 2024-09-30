# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:58:23 2024

@author: GTH025
"""

import numpy as np
import pandas as pd
import PBjammer

BigData = pd.read_csv('BigData.csv', sep=',', comment='#')
exptime = 60
Mission='K2'
Plot = True
l1 = True
Type = 'SG'

for d in range(66, 67):
    print(BigData.iloc[d,])
    Result, f, s = PBjammer.Run(ID=f'EPIC{BigData.ID[d]}', numax=(BigData.numax[d], BigData.numax_e[d]),
                          dnu=(BigData.dnu[d], BigData.dnu_e[d]), teff=(BigData.Teff[d], BigData.Teff_e[d]),
                          bp_rp=(BigData.bp_rp[d], BigData.bp_rp_e[d]), exptime=exptime, Mission=Mission, Plot=Plot, l1=l1, Type=Type)

    FinalResult = PBjammer.PeakBagger(Result, f, s, Plot=Plot)

#%%
'''
Data = pd.read_csv('Input.tsv', sep='\t', comment='#',
                   names=['ID', 'numax1', 'numax1_e', 'dnu1', 'dnu1_e', 'numax2',
                          'numax2_e', 'dnu2', 'dnu2_e', 'numax3', 'numax3_e', 'dnu3', 'dnu3_e'])

File = pd.read_csv('asu.tsv', sep='\t', comment='#', names=['ID', 'Teff1', 'Teff1_e', 'Teff2', 'Teff2_e'])

BP = pd.read_csv('asu (1).tsv', sep='\t', comment='#', names=['Source', 'bp_rp'])

#%%

# Data.drop_duplicates(subset='ID', keep='last', inplace=True)

RefinedInput = pd.DataFrame(columns=['ID', 'numax', 'numax_e', 'dnu', 'dnu_e']) 

for n in range(len(Data)):
    if Data.numax1[n] == '        ':
        print('oh')
        if Data.numax2[n] == '        ':
            print('boo')
        else:
            RefinedInput.loc[n] = [Data.ID[n]] + [Data.numax2[n]] + [Data.numax2_e[n]] + [Data.dnu2[n]] + [Data.dnu2_e[n]]
    else:
        RefinedInput.loc[n] = [Data.ID[n]] + [Data.numax1[n]] + [Data.numax1_e[n]] + [Data.dnu1[n]] + [Data.dnu1_e[n]]

#%%

RefinedTeff = pd.DataFrame(columns=['ID', 'Teff', 'Teff_e'])

for n in range(len(Data)):
    if File.Teff1[n] == '    ':
        print('oh')
        if File.Teff2[n] == '    ':
            print('boo')
        else:
            RefinedTeff.loc[n] = [File.ID[n]] + [File.Teff2[n]] + [File.Teff2_e[n]]
    else:
        RefinedTeff.loc[n] = [File.ID[n]] + [File.Teff1[n]] + [File.Teff1_e[n]]

#%%

BigData = pd.DataFrame()

BigData = pd.concat([RefinedInput, RefinedTeff.iloc[:,1:]], axis=1)

BigData = pd.concat([BigData, BP.iloc[:,1]], axis=1)

BPe = pd.DataFrame({'bp_rp_e':np.ones(173)*0.05})

BigData = pd.concat([BigData, BPe], axis=1)

BigData.to_csv('BigData.csv', index=False)

#%%

Freq = Result.get('summary').get('freq')
Height = Result.get('summary').get('height')
Width = Result.get('summary').get('width')

np.savetxt('{ID}.csv', np.array([Freq[0], Freq[1], Height[0], Height[1], Width[0], Width[1]]).T,
           delimiter=',', header='Freq, Freq_err, Height, Height_err, Width, Width_err')
'''
