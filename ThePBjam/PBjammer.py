# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:42:02 2024

@author: gth025
"""

import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pbjam import IO
from pbjam.modeID import modeID
from pbjam.peakbagging import peakbag

Directory = 'C:/Users/GTH025/Documents/PBjammy'

def PSD(ID):
    # Getting the power spectrum for the star.
    
    Lightning = pd.read_csv(f'{Directory}/LightCurves/ktwo{ID}_01_kasoc-psd_slc_v1.pow', comment='#', names=['Frequency', 'Power'], sep='   ')
    
    return np.array(Lightning.Frequency), np.array(Lightning.Power)

def Mode20(ID, Np, numax=None, dnu=None, teff=None, bp_rp=None, Plot=None, l1=None, Type=None):
    # Identifying the mode frequnecies for peakbagging.
    
    f, s = PSD(ID)

    M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, N_p=Np)
    M.runl20model()

    # Time for dipoles? or not, up to you.

    if l1:
        Dipole(M, Type)

    Result = M.result
    
    if Plot:
        M.spectrum()
        plt.savefig(f'{Directory}/Output/Small Test Data/{ID} - {Np} - Mode ID.pdf')
        M.echelle()
        plt.savefig(f'{Directory}/Output/Small Test Data/{ID} - {Np} - Echelle.pdf')

    return Result, f, s, M

def Dipole(M, Type):
    M.runl1model(model=Type)

    return M

def PeakBagger(ID, Np, Result, f, s, Plot=False):

    Peak = peakbag(f, s, ell=Result['ell'], freq=Result['summary']['freq'],
                   height=Result['summary']['height'], width=Result['summary']['width'], slices=6)
    
    Result = Peak()
    
    if Plot:
        Peak.spectrum()
        plt.savefig(f'{Directory}/Output/Small Test Data/{ID} - {Np} - Peakbagging.pdf')
        Peak.echelle()
        plt.savefig(f'{Directory}/Output/Small Test Data/{ID} - {Np} - Peakbagged Echelle.pdf')
    
    return Result, Peak

def Run(ID, Np, numax=None, dnu=None, teff=None, bp_rp=None, Plot=None, l1=None, Type=None):
    
    Result, f, s, M = Mode20(ID, Np, numax=numax, dnu=dnu, teff=teff, bp_rp=bp_rp, Plot=Plot, l1=l1, Type=Type)

    return Result, f, s, M
