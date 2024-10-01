# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:37:48 2024

@author: GTH025
"""

import matplotlib.pyplot as plt
import pickle

Directory = 'C:/Users/GTH025/Documents/PBjammy'
InputFile = f'{Directory}/Output/Peakbags/228789925.pickle'

with open(InputFile, 'rb') as File:
    LoadedData = pickle.load(File)

plt.figure()
for n in range(len(LoadedData['samples']['freq'])):
    plt.plot(LoadedData['samples']['freq'][n], LoadedData['samples']['width'][n], 'r.', markersize=0.5)
plt.show()
