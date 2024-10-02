# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:58:23 2024

@author: GTH025
"""

import pandas as pd
import PBjammer
import pickle

Directory = 'C:/Users/GTH025/Documents/PBjammy'
BigData = pd.read_csv(f'{Directory}/Input/SmallData.csv', sep=',', comment='#')
Plot = True
l1 = True
Save = True
Np = 9

def ModeResult(ID, numax, dnu, teff, bp_rp, l1, Type):
    return PBjammer.Run(ID, Np, numax=numax, dnu=dnu, teff=teff, bp_rp=bp_rp, Plot=Plot, l1=l1, Type=Type)

def Peakbagging(ID, Result, f, s):
    return PBjammer.PeakBagger(ID, Np, Result, f, s, Plot=Plot)

for d in range(len(BigData)):
    
    # Ignoring giant stars for now, with rough cut-off
    if BigData.Teff[d] < 5400:
        print('Giant Star - moving on')
        continue
    
    # Let's me know what is running right now
    print(BigData.iloc[d,])
    print(f'ID: {BigData.ID[d]}')

    # Runs for Mode ID
    Result, f, s, M = ModeResult(BigData.ID[d], (BigData.numax[d], BigData.numax_e[d]),
                                 (BigData.dnu[d], BigData.dnu_e[d]), (BigData.Teff[d], BigData.Teff_e[d]),
                                 (BigData.bp_rp[d], BigData.bp_rp_e[d]), Plot=Plot, l1=l1, Type=BigData.Type[d])
    
    # Runs for Peakbagging
    FinalResult, Peak = Peakbagging(BigData.ID[d], Result, f, s, Plot=Plot)

    # Saving the results
    if Save:
        OutputFileM = f'{Directory}/Output/ModeIDs/{BigData.ID[d]} - {BigData.Type[d]}.pickle'
        OutputFileP = f'{Directory}/Output/Peakbags/{BigData.ID[d]} - {BigData.Type[d]}.pickle'
        
        with open(OutputFileM, 'wb') as file:
            pickle.dump(FinalResult, file)
        
        with open(OutputFileP, 'wb') as file:
            pickle.dump(FinalResult, file)
