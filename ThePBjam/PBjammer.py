# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:42:02 2024

@author: gth025
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from pbjam.modeID import modeID
from pbjam.peakbagging import peakbag

Directory = 'C:/Users/GTH025/Documents/PBjammy'
Folder = f'{Directory}/Output/Plots'

def CheckSaveDir(ID):
    if not os.path.isdir(f'{Folder}/EPIC {ID}'):
        os.makedirs(f'{Folder}/EPIC {ID}')

def Model(x):
    return -7.22*10**-4*x + 5.64

def PSD(ID, Speciality):
    # Getting the power spectrum for the star.
    if Speciality == 'Standard':
        Lightning = pd.read_csv(f'{Directory}/LightCurves/ktwo{ID}_01_kasoc-psd_slc_v1.pow', comment='#', names=['Frequency', 'Power'], sep=' ')
    elif Speciality == 'Text':
        Lightning = pd.read_csv(f'{Directory}/LightCurves/{ID}_psd_tot.txt', names=['Frequency', 'Power', 'FrequencyAvg', 'PowerAvg'], sep=' ')
    elif Speciality == '3-space':
        Lightning = pd.read_csv(f'{Directory}/LightCurves/ktwo{ID}_01_kasoc-psd_slc_v1.pow', comment='#', names=['Frequency', 'Power'], sep='   ')

    return np.array(Lightning.Frequency), np.array(Lightning.Power)

def Mode20(ID, Np, numax=None, dnu=None, teff=None, bp_rp=None, Plot=None, l1=None, Type=None):
    # Identifying the mode frequnecies for peakbagging.
    try:
        f, s = PSD(ID, 'Text')

        M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, N_p=Np)
        print('Contacting Text File')
        M.runl20model()
    except:
        try:
            f, s = PSD(ID, 'Standard')

            M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, N_p=Np)
            print('Standard Configuration')
            M.runl20model()
        except:
            f, s = PSD(ID, '3-space')

            M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, N_p=Np)
            print('Activating 3-space separation')
            M.runl20model()

    # Time for dipoles? or not, up to you.

    if l1:
        Dipole(M, Type)

    Result = M.result

    # Comparing epsilon used to what it "should" have been.
    UsedEpsilon = Result['summary']['eps_p'][0]
    Epsilon = 1.45
    if teff[0] > 5800:
        Epsilon = Model(teff[0])
    print(f'Using epsilon of {UsedEpsilon}')
    print(f'Model suggests {Epsilon}')

    if Plot:
        CheckSaveDir(ID)
        print('Plotting')
        M.spectrum()
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Mode ID.pdf')
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Mode ID.png')
        M.echelle()
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Echelle.pdf')
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Echelle.png')

    return Result, f, s, M

def Dipole(M, Type):
    M.runl1model(model=Type)

    return M

def PeakBagger(ID, Np, Result, f, s, Type, Plot=False):

    Peak = peakbag(f, s, ell=Result['ell'], freq=Result['summary']['freq'],
                   height=Result['summary']['height'], width=Result['summary']['width'], slices=8)

    Result = Peak()

    if Plot:
        CheckSaveDir(ID)
        print('Plotting')
        Peak.spectrum()
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Peakbagging.pdf')
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Peakbagging.png')
        Peak.echelle()
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Peakbagged Echelle.pdf')
        plt.savefig(f'{Folder}/EPIC {ID}/{ID} - {Np} - {Type} - Peakbagged Echelle.png')

    return Result, Peak

def Run(ID, Np, numax=None, dnu=None, teff=None, bp_rp=None, Plot=None, l1=None, Type=None):

    Result, f, s, M = Mode20(ID, Np, numax=numax, dnu=dnu, teff=teff, bp_rp=bp_rp, Plot=Plot, l1=l1, Type=Type)

    return Result, f, s, M
