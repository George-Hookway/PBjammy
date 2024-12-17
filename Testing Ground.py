# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:37:39 2024

@author: GTH025
"""

#%% Plotting HR Diagram for the Keystone Sample

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('tableau-colorblind10')

Directory = 'C:/Users/GTH025/Documents/PBjammy'

BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')
SmallData = pd.read_csv(f'{Directory}/Input/SmallData.csv', sep=',', comment='#')
Luminosity = pd.read_csv(f'{Directory}/Input/Luminosities.tsv', sep='\t', comment='#')

Index = BigData[BigData.ID==228720824].index
BigData.drop(index=Index, inplace=True)
BigData.reset_index(inplace=True)

Title = 'HR Diagram of the PBjammed Stars within the Keystone Sample'
plt.figure()
for s in range(len(BigData)):
    Colour = 'red'
    Size = 5
    if BigData.Done[s] == 1:
        Colour = 'green'
        Size = 15
    elif BigData.Done[s] == 10 or BigData.Done[s] == 2:
        Colour = 'purple'
        Size = 8
    plt.errorbar(BigData.Teff[s], BigData.Lum[s], yerr=BigData.Lum_e[s], xerr=BigData.Teff_e[s],
                 fmt='.', color=Colour, markersize=Size, elinewidth=0.5, capsize=0.5)

# For the Legend
plt.errorbar(0, 0, yerr=0.1, xerr=0.1, fmt='.', color='red', markersize=5,
             elinewidth=0.5, capsize=0.5, label='Keystone Sample')
plt.errorbar(0, 0, yerr=0.1, xerr=0.1, fmt='.', color='purple', markersize=8,
             elinewidth=0.5, capsize=0.5, label='Awaiting Approval')
plt.errorbar(0, 0, yerr=0.1, xerr=0.1, fmt='.', color='green', markersize=15,
             elinewidth=0.5, capsize=0.5, label='Approved Stars')

plt.plot(5772, 1, '.', color='royalblue', label='The Sun')
plt.xscale('log')
plt.yscale('log')
plt.xlim(4592.24, 6964.6)
plt.ylim(0.698454, 32.1911)
plt.gca().invert_xaxis()
plt.title(Title)
plt.xlabel('Temperature/K')
plt.ylabel(r'Luminosity/L$_{\odot}$')
plt.legend()
plt.show()
#plt.savefig(f'{Directory}/Output/{Title}.pdf')
