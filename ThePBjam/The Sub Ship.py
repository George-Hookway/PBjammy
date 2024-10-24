# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:23:47 2024

@author: gth025
"""

import multiprocessing
import TheActivator
import traceback

def Activate(n):
    TheActivator.LetUsBegin(n)

def Stuff():
    Stars = 149
    NewStars = 24
    for n in range(Stars, Stars+NewStars):
        exec(f'Gunray_{n} = multiprocessing.Process(target=Activate, args=(n, ))')
        exec(f'Gunray_{n}.start()')

    for k in range(Stars, Stars+NewStars):
        exec(f'Gunray_{k}.join()')

Stuff()
