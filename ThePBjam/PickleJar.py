# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:11:26 2024

@author: GTH025
"""

import matplotlib.pyplot as plt
import pandas as pd
import pickle

Directory = 'G:/george/PBjammy'
BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')

#%% Automated

n = [38]

for S in n:
    # Mode ID stage
    print(f'EPIC {BigData.ID[S]}')
    if BigData.Type[S] == 'MS' :
        print('Not a giant, thought you ought to know')
        #continue
    try:
        with open(f'{Directory}/Output/ModeIDs/{BigData.ID[S]} - {BigData.Np[S]} - '
                  f'{BigData.Type[S]} - Raw.pickle', 'rb') as File:
            Data = pickle.load(File)
        Data.echelle()
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Echelle.pdf')
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Echelle.png')
        plt.close()
        Data.spectrum()
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Mode ID.pdf')
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Mode ID.png')
        plt.close()
        File.close()
    except:
        print(f'No ModeID data for star EPIC {BigData.ID[S]}')
        continue

    # Peakbagged Stage
    try:
        with open(f'{Directory}/Output/Peakbags/{BigData.ID[S]} - {BigData.Np[S]} - '
                  f'{BigData.Type[S]} - Raw.pickle', 'rb') as File:
            Data = pickle.load(File)
        Data.echelle()
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Peakbagged Echelle.pdf')
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Peakbagged Echelle.png')
        plt.close()
        Data.spectrum()
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Peakbagging.pdf')
        plt.savefig(f'{Directory}/Output/Plots/EPIC {BigData.ID[S]}/{BigData.ID[S]} - '
                    f'{BigData.Np[S]} - {BigData.Type[S]} - Peakbagging.png')
        plt.close()
        File.close()
    except:
        print(f'No peakbagged data for star EPIC {BigData.ID[S]}')
        continue

#%% Manual
'''
Star = 38

with open(f'{Directory}/Output/ModeIDs/{BigData.ID[Star]} - {BigData.Np[Star]} - '
          f'{BigData.Type[Star]} - Raw.pickle', 'rb') as File:
    Data = pickle.load(File)
Data.echelle()
#Data.spectrum()
Answer = Data.result
File.close()

with open(f'{Directory}/Output/Peakbags/{BigData.ID[Star]} - {BigData.Np[Star]} - '
          f'{BigData.Type[Star]} - Raw.pickle', 'rb') as File:
    Data = pickle.load(File)
#Data.echelle()
Data.spectrum()
File.close()
'''
