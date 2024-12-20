#!/usr/bin/env bash
#SBATCH --nodes 1
#SBATCH --ntasks 16
#SBATCH --qos bbdefault
#SBATCH --time 05:00:00
#SBATCH --mem 32G
#SBATCH --account=nielsemb-plato-peakbagging

module purge
module load bluebear
module load Python

python -u 'Star 0.py'
