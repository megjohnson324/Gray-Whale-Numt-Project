#!/bin/bash
#SBATCH --job-name=repeatmasker2
#SBATCH -A highmem
#SBATCH -N 1
#SBATCH -n 64
#SBATCH -t 1-00:00:00
#SBATCH --error=repeatmodeler2.err
#SBATCH --output=repeatmodeler2.out
#SBATCH --mail-user=john2788@purdue.edu
#SBATCH --mail-type=START,END,FAIL

module --force purge
ml biocontainers repeatmasker

#repeatmasker with gray whale genome
RepeatMasker -pa 64 -gff -qq -species mammals GCA_028021215.1_mEscRob2.pri_genomic.fna
