#!/usr/bin/env bash
#SBATCH --nodes 1
#SBATCH --ntasks 1
#SBATCH --qos bbdefault
#SBATCH --time 00:01:00
#SBATCH --mem 4G
#SBATCH --account=nielsemb-plato-peakbagging

module purge
module load bluebear
module load Python

python -u 'The Sister Ship.py'
