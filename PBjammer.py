# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:42:02 2024

@author: gth025
"""
Np = 8
import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
from pbjam import IO
from pbjam.modeID import modeID
from pbjam.peakbagging import peakbag

def PSD(ID=None, numax=None, dnu=None, exptime=None, Mission=None, Plot=False):
    # Getting the power spectrum for the star.
    
    print(ID)
    psd = IO.psd(ID, lk_kwargs={'exptime': exptime, 'mission':Mission, 'author':Mission}, use_cached=True)
     
    psd()

    f = psd.freq

    s = psd.powerdensity
    
    downsampling = 1
    f2 = f[::downsampling]
    s2 = s[::downsampling]
    
    # Used to get plots of the light curve for inspection. Just interesting is all.
    
    Curve = lk.search_lightcurve(ID, mission=Mission, author=Mission, exptime=exptime).download_all()
    lc = Curve.stitch().normalize().flatten(window_length=401).remove_outliers(4)

    pig = lc.to_periodogram(normalization='psd',
                            minimum_frequency=numax[0] - dnu[0] * 4,
                            maximum_frequency=numax[0] + dnu[0] * 4).flatten()

    fpig = pig.frequency
    spig = pig.power
    
    #if Plot:
        #lc.plot()
        #pig.plot()
        #plt.savefig(f'LightCurves/{ID}.png')
    
    return f, s, f2, s2

def Mode20(ID=None, numax=None, dnu=None, teff=None, bp_rp=None, exptime=None, Mission=None, Plot=None, l1=None, Type=None):
    # Identifying the mode frequnecies for peakbagging.
    
    f, s, f2, s2 = PSD(ID=ID, numax=numax, dnu=dnu, exptime=exptime, Mission=Mission, Plot=Plot)

    M = modeID(f2, s2, {'teff':teff, 'bp_rp':bp_rp, 'numax':numax, 'dnu':dnu}, N_p=Np)
    M.runl20model()

    # Time for dipoles? or not, up to you.

    if l1:
        Dipole(M, Type)

    Result = M.result
    
    if Plot:
        M.spectrum()
        plt.savefig(f'Lightning 2/SG - Mode ID.pdf')
        M.echelle()
        plt.savefig(f'Lightning 2/SG - Echelle.pdf')
    
    return Result, f, s

def Dipole(M, Type):
    M.runl1model(model=Type)

    return M

def PeakBagger(Result, f, s, Plot=False):
    
    Peak = peakbag(f, s, ell=Result['ell'], freq=Result['summary']['freq'],
                   height=Result['summary']['height'], width=Result['summary']['width'], slices=6)
    
    Result = Peak()
    
    if Plot:
        Peak.spectrum()
        plt.savefig(f'Lightning 2/SG - Peakbagging.pdf')
    
    return Result

def Run(ID=None, numax=None, dnu=None, teff=None, bp_rp=None, exptime=None, Mission=None, Plot=None, l1=None, Type=None):
    Result, f, s = Mode20(ID=ID, numax=numax, dnu=dnu, teff=teff, bp_rp=bp_rp,
                    exptime=exptime, Mission=Mission, Plot=Plot, l1=l1, Type=Type)
    
    #Result, f, s, Poo = PSD(ID=ID, numax=numax, dnu=dnu, exptime=exptime, Mission=Mission, Plot=Plot)

    return Result, f, s
