# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:03:25 2024

@author: gth025
"""

for Number in range(0, 173):
    Text = f'#!/usr/bin/env bash\n#SBATCH --nodes 1\n#SBATCH --ntasks 1\n#SBATCH --qos bbdefault\n#SBATCH --time 05:00:00\n#SBATCH --mem 32G\n#SBATCH --account=nielsemb-plato-peakbagging\n\nmodule purge\nmodule load bluebear\nmodule load Python\n\npython -u \'Star {Number}.py\''

    with open(f'G:/george/PBjammy/ThePBjam/Runner{Number}.sh', 'w', newline='\n') as File:
        File.write(Text)
    File.close()
