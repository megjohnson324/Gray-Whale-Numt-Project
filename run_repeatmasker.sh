#This script runs the RepeatMasker program on the gray whale genome file with a specification to output a GFF file to be used in later analysis.
#RepeatMasker is a program that screens a genome and provides an output of repeats in the genome file. 
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
#include -gff if you want a gff file output format
RepeatMasker -pa 64 -gff -qq -species mammals GCA_028021215.1_mEscRob2.pri_genomic.fna
