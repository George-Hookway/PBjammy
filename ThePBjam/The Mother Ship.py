# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:53:25 2024

@author: GTH025
"""

for Number in range(0, 173):
    Text = f'import TheActivator\n\nTheActivator.LetUsBegin({Number})\n'

    with open(f'G:/george/PBjammy/ThePBjam/Star {Number}.py', 'w') as File:
        File.write(Text)
    File.close()
