# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:42:02 2024

@author: gth025
"""

import lightkurve as lk
import matplotlib.pyplot as plt
from pbjam import IO
from pbjam.modeID import modeID
from pbjam.peakbagging import peakbag

Np = 9
Directory = 'C:/Users/GTH025/Documents/PBjammy'
SaveName = f'Lightning McQueen/{Np}'

def PSD(ID=None, numax=None, dnu=None, exptime=None, Mission=None, Plot=False):
    # Getting the power spectrum for the star.
    
    print(ID)
    psd = IO.psd(ID, lk_kwargs={'exptime': exptime, 'mission':Mission, 'author':Mission}, use_cached=True)
     
    psd()

    f = psd.freq

    s = psd.powerdensity
    
    return f, s

def Mode20(ID=None, numax=None, dnu=None, teff=None, bp_rp=None, exptime=None, Mission=None, Plot=None, l1=None, Type=None):
    # Identifying the mode frequnecies for peakbagging.
    
    f, s = PSD(ID=ID, numax=numax, dnu=dnu, exptime=exptime, Mission=Mission, Plot=Plot)

    M = modeID(f, s, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, N_p=Np)
    M.runl20model()

    # Time for dipoles? or not, up to you.

    if l1:
        Dipole(M, Type)

    Result = M.result
    
    if Plot:
        M.spectrum()
        #plt.savefig(f'{Directory}/Output/{SaveName} - Mode ID.pdf')
        M.echelle()
        #plt.savefig(f'{Directory}/Output/{SaveName} - Echelle.pdf')
    
    return Result, f, s, M

def Dipole(M, Type):
    M.runl1model(model=Type)

    return M

def PeakBagger(Result, f, s, Plot=False):
    
    Peak = peakbag(f, s, ell=Result['ell'], freq=Result['summary']['freq'],
                   height=Result['summary']['height'], width=Result['summary']['width'], slices=6)
    
    Result = Peak()
    
    if Plot:
        Peak.spectrum()
        #.savefig(f'{Directory}/Output/{SaveName} - Peakbagging.pdf')
        Peak.echelle()
        #plt.savefig(f'{Directory}/Output/{SaveName} - Peakbagging.pdf')
    
    return Result, Peak

def Run(ID=None, numax=None, dnu=None, teff=None, bp_rp=None, exptime=None, Mission=None, Plot=None, l1=None, Type=None):
    Result, f, s, M = Mode20(ID=ID, numax=numax, dnu=dnu, teff=teff, bp_rp=bp_rp,
                    exptime=exptime, Mission=Mission, Plot=Plot, l1=l1, Type=Type)

    return Result, f, s, M
