# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:03:25 2024

@author: gth025
"""

import multiprocessing
import TheActivator
import traceback

def Activate(n):
    TheActivator.LetUsBegin(n)

def Stuff():
    Stars = 66
    NewStars = 66
    for n in range(Stars, Stars+NewStars):
        exec(f'Gunray_{n} = multiprocessing.Process(target=Activate, args=(n, ))')
        exec(f'Gunray_{n}.start()')

    for k in range(Stars, Stars+NewStars):
        exec(f'Gunray_{k}.join()')

Stuff()
