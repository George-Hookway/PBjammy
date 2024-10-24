# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:53:25 2024

@author: GTH025
"""

import multiprocessing
import TheActivator
import traceback

def Activate(n):
    TheActivator.LetUsBegin(n)

def Stuff():
    Stars = 66
    for n in range(Stars):
        exec(f'Gunray_{n} = multiprocessing.Process(target=Activate, args=(n, ))')
        exec(f'Gunray_{n}.start()')

    for k in range(Stars):
        exec(f'Gunray_{k}.join()')

Stuff()
