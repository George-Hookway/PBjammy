# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:52:20 2024

@author: gth025
"""

import pandas as pd
import PBjammer
import pickle

Directory = 'G:/george/PBjammy'
SaveDirectory = 'C:/Users/GTH025/Documents/PBjammy'
BigData = pd.read_csv(f'{Directory}/Input/BigData.csv', sep=',', comment='#')

for Star in range(len(BigData)):
    print(BigData.ID[Star])
    try:
        with open(f'{Directory}/Output/Peakbags/{BigData.ID[Star]} - {BigData.Np[Star]} - '
                  f'{BigData.Type[Star]}.pickle', 'rb') as File:
            Data = pickle.load(File)
        
        with open(f'{SaveDirectory}/Output/Peakbags/{BigData.ID[Star]} - {BigData.Np[Star]}'
                  f' - {BigData.Type[Star]}.pickle', 'wb') as file:
            pickle.dump(Data, file)
        file.close()
        File.close()
    except:
        print('I don\'t think so!')
