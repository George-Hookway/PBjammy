# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:34:09 2024

@author: GTH025
"""

import matplotlib.pyplot as plt
import numpy as np
import PBjammer

def TotalDestruction(LightCurve):

    Frequencies = [47.2, 94.5, 141.7, 188.9, 236.1, 283.2, 330.4, 377.6, 424.8, 472.0, 519.2, 566.4, 613.6, 660.8]

    print('Total Extermination!')
    HitList = []
    for n in range(len(LightCurve[0])):
        for f in Frequencies:
            Cut = 1
            #if f == 613.6:
            #    Cut = 2
            #if LightCurve[0][n] > f-Cut and LightCurve[0][n] < f+Cut:
            #    HitList.append(n)
        #if LightCurve[0][n] > 2068 and LightCurve[0][n] < 2145:
        #    HitList.append(n)
    print(HitList)
    Freq = np.delete(LightCurve[0], HitList)
    Power = np.delete(LightCurve[1], HitList)

    return Freq, Power
