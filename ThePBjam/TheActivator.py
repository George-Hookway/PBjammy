# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:58:23 2024

@author: GTH025
"""

import datetime
import pandas as pd
import PBjammer
import pickle
import sys
import traceback

#Directory = 'C:/Users/GTH025/Documents/PBjammy'
Directory = '/rds/projects/n/nielsemb-plato-peakbagging/george/PBjammy'
#Directory = 'G:/george/PBJammy'
BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')
#BigData = pd.read_csv('/rds/projects/n/nielsemb-plato-peakbagging/george/Sinister Six/StarList.csv', sep=',', comment='#')
Plot = False
l1 = True
Save = True

def ModeResult(ID, Np, numax, dnu, teff, bp_rp, Type):
    return PBjammer.Run(ID, Np, numax=numax, dnu=dnu, teff=teff, bp_rp=bp_rp, Plot=Plot, l1=l1, Type=Type)

def Peakbagging(ID, Np, Result, f, s, Type):
    return PBjammer.PeakBagger(ID, Np, Result, f, s, Type, Plot=Plot)

def Activate(n):
    for d in range(n, n+1):

        # Ignoring stars that are "done"
        if BigData.Flag[d] == 1:
            print('You already did this one.\nMove along?\n')
            #continue

        elif BigData.Flag[d] == 2:
            print('I\'ve approved it, so we\'ll leave it for now :)\n')

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
            OutputFileMRaw = f'{Directory}/Output/ModeIDs/{BigData.ID[d]} - {BigData.Np[d]} - {BigData.Type[d]} - Raw.pickle'
            OutputFileP = f'{Directory}/Output/Peakbags/{BigData.ID[d]} - {BigData.Np[d]} - {BigData.Type[d]}.pickle'
            OutputFilePRaw = f'{Directory}/Output/Peakbags/{BigData.ID[d]} - {BigData.Np[d]} - {BigData.Type[d]} - Raw.pickle'

            with open(OutputFileM, 'wb') as file:
                pickle.dump(Result, file)
            file.close()

            with open(OutputFileMRaw, 'wb') as file:
                pickle.dump(M, file)
            file.close()
            
            with open(OutputFileP, 'wb') as file:
                pickle.dump(FinalResult, file)
            file.close()

            with open(OutputFilePRaw, 'wb') as file:
                pickle.dump(Peak, file)
            file.close()
            
    print('Calculation Complete')

def LetUsBegin(n):
    PBjammer.CheckSaveDir(BigData.ID[n])
    stdoutOrigin=sys.stdout
    sys.stdout = open(f'{Directory}/Output/Plots/EPIC {BigData.ID[n]}/MrFibuli.txt', 'a')

    try:
        print(datetime.datetime.now().strftime("%c"))
        Activate(n)
        print('\n')
        
        sys.stdout.close()
        sys.stdout=stdoutOrigin
    except:
        with open(f'{Directory}/Output/Plots/EPIC {BigData.ID[n]}/MrFibuli.txt', "a") as logfile:
            traceback.print_exc(file=logfile)
            print('\n')
            sys.stdout.close()
            sys.stdout=stdoutOrigin
        raise

#LetUsBegin(41)
