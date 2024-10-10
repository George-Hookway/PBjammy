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

Title = 'HR Diagram of the Completed Stars within the Keystone Sample'
plt.figure()
for s in range(len(BigData)):
    Colour = 'red'
    Size = 5
    if BigData.Done[s] == 1:
        Colour = 'green'
        Size = 12
    plt.errorbar(BigData.Teff[s], BigData.Lum[s], yerr=BigData.Lum_e[s], xerr=BigData.Teff_e[s],
                 fmt='.', color=Colour, markersize=Size, elinewidth=0.5, capsize=0.5, label='Keystone Dataset')
plt.plot(5772, 1, '.', color='royalblue', label='The Sun')
plt.gca().invert_xaxis()
plt.xscale('log')
plt.yscale('log')
plt.title(Title)
plt.xlabel('Temperature/K')
plt.ylabel(r'Luminosity/L$_{\odot}$')
#plt.legend()
plt.show()
#plt.savefig(f'{Directory}/Output/{Title}.pdf')
