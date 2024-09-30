# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:37:39 2024

@author: GTH025
"""

#%% Plotting HR Diagram for the Keystone Sample

import matplotlib.pyplot as plt
import pandas as pd

BigData = pd.read_csv('BigData.csv', sep=',', comment='#')
Luminosity = pd.read_csv('Luminosities.tsv', sep='\t', comment='#')

Index = BigData[BigData.ID==228720824].index
BigData.drop(index=Index, inplace=True)

plt.figure()
plt.errorbar(BigData.Teff, Luminosity.Lum, yerr=Luminosity.Lum_e, xerr=BigData.Teff_e,
             fmt='.', color='red', elinewidth=0.5, capsize=0.5, label='Keystone Dataset')
plt.plot(5772, 1, '.', color='royalblue', label='The Sun')
plt.gca().invert_xaxis()
plt.xscale('log')
plt.yscale('log')
plt.title('HR Diagram of the Keystone Sample')
plt.xlabel('Temperature/K')
plt.ylabel(r'Luminosity/L$_{\odot}$')
plt.legend()
plt.show()

#%% Looking at the results for KIC 5184732

import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv('KIC5184732.csv', sep=',')
