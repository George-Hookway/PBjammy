# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:37:39 2024

@author: GTH025
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


Directory = 'G:/george/PBjammy'

BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')
SmallData = pd.read_csv(f'{Directory}/Input/SmallData.csv', sep=',', comment='#')
Luminosity = pd.read_csv(f'{Directory}/Input/Luminosities.tsv', sep='\t', comment='#')

Index = BigData[BigData.ID==228720824].index
BigData.drop(index=Index, inplace=True)
BigData.reset_index(inplace=True)

#%% Standard HR Diagram
Colour = ['royalblue', 'skyblue', 'forestgreen', 'black', 'orange', 'orange', 'red', 'magenta', 'grey', 'pink']
Flags = ['Approved', 'purgatory', 'Pending', 'Dead', 'dnu or epsilon', 'dnu or epsilon', 'Systematics', 'Noisy', 'Np', 'g-modes']


Title = 'HR Diagram of the PBjammed Stars within the Keystone Sample'
plt.figure()

for s in range(len(BigData)):
    for f in range(1, 11):
        FMT = '.'
        Size = 5
        if BigData.Binary[s] == 1:
            FMT = 'X'
        if BigData.Flag[s] == f:
            plt.errorbar(BigData.Teff[s], BigData.Lum[s], yerr=BigData.Lum_e[s], xerr=BigData.Teff_e[s],
                         fmt=FMT, color=Colour[f-1], markersize=Size, elinewidth=0.5, capsize=0.5)

# For the Legend
for l in range(len(Colour)):
    if l == 5:
        continue
    plt.errorbar(np.nan, np.nan, yerr=np.nan, xerr=np.nan,
                 fmt='.', color=Colour[l], markersize=Size, elinewidth=0.5, capsize=0.5, label=Flags[l])
plt.errorbar(np.nan, np.nan, xerr=np.nan,
             fmt='X', color='royalblue', markersize=8, elinewidth=0.5, capsize=0.5, label='Potential Binaries')

plt.plot(5772, 1, '*', color='darkorange')
plt.plot([6250, 6900], [7.4, 10.5], '--', color='black', alpha=0.7, label='Sub-giant boundaries')
plt.plot([5050, 6250], [0.76, 7.4], '--', color='black', alpha=0.7)
plt.plot([4800, 5500], [0.88, 23.2], '--', color='black', alpha=0.7)
#plt.xscale('log')
plt.yscale('log')
#plt.xlim(4592.24, 6964.6)
#plt.ylim(0.698454, 32.1911)
plt.gca().invert_xaxis()
plt.title(Title)
plt.xlabel('Temperature/K')
plt.ylabel(r'Luminosity/L$_{\odot}$')
#plt.legend()
plt.show()
plt.savefig(f'{Directory}/Output/Plots/{Title}.pdf')
plt.close()

#%% MS-SG-RGB Diagram

Colour = ['royalblue', 'orange', 'magenta']
Flags = ['MS', 'SG', 'RGB']

Title = 'HR Diagram of the different star types within the Keystone Sample'
plt.figure()

for s in range(len(BigData)):
    for f in range(0, 3):
        FMT = '.'
        Size = 5
        if BigData.Binary[s] == 1:
            FMT = 'X'
        if BigData.Type[s] == Flags[f]:
            plt.errorbar(BigData.Teff[s], BigData.Lum[s], yerr=BigData.Lum_e[s], xerr=BigData.Teff_e[s],
                         fmt=FMT, color=Colour[f], markersize=Size, elinewidth=0.5, capsize=0.5)

# For the Legend
for l in range(len(Colour)):
    plt.errorbar(np.nan, np.nan, yerr=np.nan, xerr=np.nan,
                 fmt='.', color=Colour[l], markersize=Size, elinewidth=0.5, capsize=0.5, label=Flags[l])
plt.errorbar(np.nan, np.nan, xerr=np.nan,
             fmt='X', color='royalblue', markersize=8, elinewidth=0.5, capsize=0.5, label='Potential Binaries')

plt.plot(5772, 1, '*', color='darkorange')
plt.yscale('log')
plt.gca().invert_xaxis()
plt.title(Title)
plt.xlabel('Temperature/K')
plt.ylabel(r'Luminosity/L$_{\odot}$')
plt.legend()
plt.show()
plt.savefig(f'{Directory}/Output/Plots/{Title}.pdf')
plt.close()

#%% Deltanu vs numax

plt.figure()
plt.errorbar(BigData.dnu, BigData.numax, yerr=BigData.numax_e, xerr=BigData.dnu_e, 
             fmt='.', elinewidth=0.5, capsize=0.5)
plt.xlabel(r'$\Delta\nu$')
plt.ylabel(r'$\nu_{max}$')
plt.show()
plt.close()
