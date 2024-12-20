# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:42:02 2024

@author: gth025
"""

import Exterminate
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pbjam.distributions as dist
import pbjam.IO as IO
from pbjam.modeID import modeID
from pbjam.peakbagging import peakbag

#Directory = 'C:/Users/GTH025/Documents/PBjammy'
Directory = '/rds/projects/n/nielsemb-plato-peakbagging/george/PBjammy'
#Directory = 'G:/george/PBJammy'
Folder = f'{Directory}/Output/Plots'

def CheckSaveDir(ID, folder=Folder):
    if not os.path.isdir(f'{folder}/EPIC {ID}'):
        os.makedirs(f'{folder}/EPIC {ID}')

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

    #psd = IO.psd(ID=ID, lk_kwargs={}, time=Lightning.Frequency, flux=Lightning.Power)

    #psd()

    Destroy = Exterminate.TotalDestruction([np.array(Lightning.Frequency), np.array(Lightning.Power)])

    return Destroy[0], Destroy[1]

def Mode20(ID, Np, numax=None, dnu=None, teff=None, bp_rp=None, Plot=None, l1=None, Type=None):
    # Identifying the mode frequnecies for peakbagging.

    # Comparing epsilon used to what it "should" have been.
    Epsilon = 1.45
    if teff[0] > 5800:
        Epsilon = Model(teff[0])

    Priors = {}
    # 'dnu': dist.normal(loc=np.log10(dnu[0]), scale=dnuScale)
    # 'numax': dist.normal(loc=np.log10(numax[0]), scale=numaxScale)
    # 'eps_p': dist.normal(loc=Epsilon, scale=EpsilonScale)
    # 'eps_g': dist.normal(loc=0.8, scale=gEpsilonScale)
    # 'd01': dist.normal(loc=np.log10(dnu[0]/2), scale=d01Scale)
    dnuScale = 0.0015
    numaxScale = 0.02
    EpsilonScale = 0.01
    gEpsilonScale = 0.2
    d01Scale = 0.5
    #Priors = {'dnu': dist.normal(loc=np.log10(dnu[0]), scale=dnuScale),
    #          'numax': dist.normal(loc=np.log10(numax[0]), scale=numaxScale),
    #          'eps_p': dist.normal(loc=Epsilon, scale=EpsilonScale)}
    print(f'{dnuScale}, {numaxScale}, {EpsilonScale}, {gEpsilonScale}, {d01Scale}')
    print(Priors)
    try:
        print('Contacting Text File')
        f, s = PSD(ID, 'Text')
        M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, addPriors=Priors, N_p=Np)
        M.runl20model()
    except:
        try:
            print('Standard Configuration')
            f, s = PSD(ID, 'Standard')

            M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, addPriors=Priors, N_p=Np)
            M.runl20model()
        except:
            print('Activating 3-space separation')
            f, s = PSD(ID, '3-space')

            M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, addPriors=Priors, N_p=Np)
            M.runl20model()

    # Time for dipoles? or not, up to you.

    if l1:
        Dipole(M, Type)

    Result = M.result

    UsedEpsilon = Result['summary']['eps_p'][0]
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
    M.runl1model(model=Type, PCAsamples=500)

    return M

def PeakBagger(ID, Np, Result, f, s, Type, Plot=False):

    Peak = peakbag(f, s, ell=Result['ell'], freq=Result['summary']['freq'],
                   height=Result['summary']['height'], width=Result['summary']['width'], slices=1)

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
