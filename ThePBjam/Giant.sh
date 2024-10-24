#!/usr/bin/env bash
#SBATCH --nodes 1
#SBATCH --ntasks 17
#SBATCH --qos bbdefault
#SBATCH --time 05:00:00
#SBATCH --mem 64G
#SBATCH --account=nielsemb-plato-peakbagging

module purge
module load bluebear
module load Python

python -u 'The Giant Ship.py'
