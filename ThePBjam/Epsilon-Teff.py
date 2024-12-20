# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:49:59 2024

@author: gth025
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

Directory = 'G:/george/PBjammy'
BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')

#%% Plot epsilons

Epsilons = pd.read_csv(f'{Directory}/Output/Epsilons.csv')

plt.figure()
for c in range(len(Epsilons)):
    Row = BigData[BigData.ID == Epsilons.ID[c]]
    Colour = 'blue'
    if Row.Type[Row.Type.index[0]] == 'SG':
        Colour = 'orange'
        continue
    elif Row.Type[Row.Type.index[0]] == 'RGB':
        Colour = 'magenta'
        continue
    plt.errorbar(Row.Teff, Epsilons.Epsilon[c], xerr=Row.Teff_e,
                 yerr=Epsilons.Epsilon_e[c], fmt='.', color=Colour)

# For the legend
plt.errorbar(np.nan, np.nan, yerr=np.nan, xerr=np.nan,
             fmt='.', color='blue', elinewidth=0.5, capsize=0.5, label='Main sequence')
plt.errorbar(np.nan, np.nan, yerr=np.nan, xerr=np.nan,
             fmt='.', color='orange', elinewidth=0.5, capsize=0.5, label='Sub-giant')
plt.errorbar(np.nan, np.nan, yerr=np.nan, xerr=np.nan,
             fmt='.', color='magenta', elinewidth=0.5, capsize=0.5, label='Red Giant')

plt.xlabel(r'$T_{eff}$/K')
plt.ylabel(r'$\epsilon$')
plt.legend()
plt.show()

#%% Plot visibility

plt.figure()
for S in range(173):
    print(BigData.ID[S])
    if BigData.Type[S] == 'RGB' or BigData.Type[S] == 'SG':
        continue
    try:
        with open(f'{Directory}/Output/Peakbags/{BigData.ID[S]} - {BigData.Np[S]} - '
                  f'{BigData.Type[S]}.pickle', 'rb') as File:
            Data = pickle.load(File)

        Area0 = 0
        Area2 = 0
        for A in range(4):
            Np = int(len(Data['summary']['height'][0])/3)
            Area2 += (Data['summary']['height'][0][int(5*Np/2)-2+A]*
                      Data['summary']['width'][0][int(5*Np/2)-2+A]/2)**2
            Area0 += (Data['summary']['height'][0][3*int(Np/2)-2+A]*
                      Data['summary']['width'][0][3*int(Np/2)-2+A]/2)**2

        V2 = Area2/Area0
        plt.plot(BigData.numax[S], V2, 'b.')
        File.close()
    except:
        print('Bother!')

plt.show()

#%% Acquire epsilons
'''
ID = []
Epsilon = []
Temperature = []
TempError = []

for n in range(173):
    if BigData.Type[n] != 'MS':
        print('Giant star')
        continue
    print(BigData.ID[n])
    try:
        with open(f'{Directory}/Output/ModeIDs/{BigData.ID[n]} - {BigData.Np[n]} - {BigData.Type[n]}.pickle', 'rb') as File:
            Data = pickle.load(File)
        Epsilon.append(Data['summary']['eps_p'])
        ID.append(BigData.ID[n])
        Temperature.append(BigData.Teff[n])
        TempError.append(BigData.Teff_e[n])
    except:
        print('Trouble!')

Eps = pd.DataFrame()
Eps.insert(0, 'ID', ID)
Eps.insert(1, 'Epsilon', np.array(Epsilon)[:,0])
Eps.insert(2, 'Epsilon_e', np.array(Epsilon)[:,1])
Eps.insert(3, 'Teff', Temperature)
Eps.insert(4, 'Teff_e', TempError)
Eps.to_csv(f'{Directory}/Output/Epsilons.csv', index=False)
'''
