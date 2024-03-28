#!/bin/bash
#SBATCH --job-name=randomsequence_comparison
#SBATCH -A fnrdewoody
#SBATCH -N 1
#SBATCH -n 64
#SBATCH -t 5-00:00:00
#SBATCH --error=randomsequence_comparison.err
#SBATCH --mail-user=john2788@purdue.edu
#SBATCH --mail-type=START,END,FAIL

module load biocontainers
module load biopython

#python randomsequence_numtcomparison.py
python randomsequence_numtcomparison.py
