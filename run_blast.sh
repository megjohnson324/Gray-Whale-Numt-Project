#!/bin/bash
#SBATCH --job-name=blast 
#SBATCH -A fnrdewoody
#SBATCH -N 1
#SBATCH -n 64
#SBATCH -t 00:30:00
#SBATCH --error=align2.err
#SBATCH --output=align2.out
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=allen715@purdue.edu

cd /scratch/bell/dewoody/graywhale_numts/

module load biocontainers
module load blast/2.13.0

# Set paths to input and output files
genome_file="GCA_028021215.1_mEscRob2.pri_genomic.fna"
query_file="gray_whale_mitogenome.fa"
output_file="blast_hits_seq.csv" # Change the output file extension to .csv

# Create a Blast database from the genome file
#makeblastdb -in "$genome_file" -dbtype nucl

# Perform Blastn alignment between query and database with CSV output format
# output headers: query id, subject id, percent identity, alignment length, mismatches, gap opens, query start, query end, subject start, subject end, e-value, bit score 
#blastn -query "$query_file" -subject "$genome_file" -out "$output_file" -outfmt "10 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore" -evalue 10

#modified to include blast hit sequences, qseq = query (mito), sseq = subject (genome), for blast hits, use sseq
blastn -query "$query_file" -subject "$genome_file" -out "$output_file" -outfmt "10 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -evalue 10

echo "Alignment completed!"
