# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:58:23 2024

@author: GTH025
"""

import pandas as pd
import PBjammer
import pickle

Directory = 'C:/Users/GTH025/Documents/PBjammy'
BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')
Plot = True
l1 = True
Save = True

def ModeResult(ID, Np, numax, dnu, teff, bp_rp, Type):
    return PBjammer.Run(ID, Np, numax=numax, dnu=dnu, teff=teff, bp_rp=bp_rp, Plot=Plot, l1=l1, Type=Type)

def Peakbagging(ID, Np, Result, f, s, Type):
    return PBjammer.PeakBagger(ID, Np, Result, f, s, Type, Plot=Plot)

for d in range(167, 168):

    # Ignoring stars that are "done"
    if BigData.Done[d] == 1:
        print('You already did this one.\nMove along\n')
        continue

    # Let's me know what is running right now
    print(BigData.iloc[d,])
    print(f'ID: {BigData.ID[d]}')

    # Runs for Mode ID
    Result, f, s, M = ModeResult(BigData.ID[d], BigData.Np[d], (BigData.numax[d], BigData.numax_e[d]),
                                 (BigData.dnu[d], BigData.dnu_e[d]), (BigData.Teff[d], BigData.Teff_e[d]),
                                 (BigData.bp_rp[d], BigData.bp_rp_e[d]), BigData.Type[d])

    # Runs for Peakbagging
    FinalResult, Peak = Peakbagging(BigData.ID[d], BigData.Np[d], Result, f, s, BigData.Type[d])

    # Saving the results
    if Save:
        print('Saving....')
        OutputFileM = f'{Directory}/Output/ModeIDs/{BigData.ID[d]} - {BigData.Np[d]} - {BigData.Type[d]}.pickle'
        OutputFileP = f'{Directory}/Output/Peakbags/{BigData.ID[d]} - {BigData.Np[d]} - {BigData.Type[d]}.pickle'

        with open(OutputFileM, 'wb') as file:
            pickle.dump(FinalResult, file)

        with open(OutputFileP, 'wb') as file:
            pickle.dump(FinalResult, file)

print('Calculation Complete')
