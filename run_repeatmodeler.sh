#!/bin/bash
#SBATCH --job-name=repeatmasker
#SBATCH -A fnrdewoody
#SBATCH -N 1
#SBATCH -n 64
#SBATCH -t 6-00:00:00
#SBATCH --error=repeatmodeler.err
#SBATCH --output=repeatmodeler.out
#SBATCH --mail-user=allen715@purdue.edu
#SBATCH --mail-type=END,FAIL

module --force purge
ml biocontainers repeatmasker
ml repeatmodeler

# make a directory for storing logs
mkdir -p logs

# build new RepeatModeler BLAST database with a name that includes an ID (e.g., a species code, specimen ID, etc.) 
# and genus/species. Modify accordingly.
BuildDatabase -name GCA_028021215.1_Gray-whale -engine ncbi GCA_028021215.1_mEscRob2.pri_genomic.fna

# now run RepeatModeler with 16 cores and send results from STDOUT and STDERR streams to 1_repeatmodeler.log
# in my experience, this command takes 1-3 days with vertebrate genomes
RepeatModeler -pa 64 -engine ncbi -database GCA_028021215.1_Gray-whale 2>&1 | tee 00_repeatmodeler.log
