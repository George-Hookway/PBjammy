#!/usr/bin/env bash
#SBATCH --nodes 1
#SBATCH --ntasks 24
#SBATCH --qos bbdefault
#SBATCH --time 10:00:00
#SBATCH --mem 96G
#SBATCH --account=nielsemb-plato-peakbagging

module purge
module load bluebear
module load Python

python -u 'The Sub Ship.py'
