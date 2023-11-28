#!/bin/bash
#SBATCH --job-name=test_repeatmodeler
#SBATCH -A debug
#SBATCH -N 1
#SBATCH -n 64
#SBATCH -t 00:30:00
#SBATCH --error=repeatmodeler.err
#SBATCH --output=repeatmodeler.out

module --force purge
ml biocontainers repeatmasker

#trying repeatmasker with gray whale genome
RepeatMasker -pa 64 -qq -species mammals GCA_028021215.1_mEscRob2.pri_genomic.fna
