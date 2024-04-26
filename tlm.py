#This script gives the sequences of any generated random sequences that are within 5000 bp of each end of each chromosome to examine the sequences for inclusion of telomeres
def load_genome_sequences(genome_file):
    genome_sequences = {}
    current_chromosome = None
    with open(genome_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                current_chromosome = line.strip().split()[0]  # Extract only the chromosome identifier
                genome_sequences[current_chromosome] = ""
            else:
                genome_sequences[current_chromosome] += line.strip()        
    return genome_sequences


def extract_sequences_in_boundary(random_seq_file, genome_file, output_file):
    genome_sequences = load_genome_sequences(genome_file)
    
    with open(random_seq_file, 'r') as f, open(output_file, 'w') as out_f:
        out_f.write("NUMT_ID,Chromosome,Sequence\n")
        for line in f:
            if line.startswith("NUMT_ID"):
                continue
            parts = line.strip().split(',')
            numt_id, chromosome = parts[:2]
            chromosome = chromosome.split()[0]  # Extract only the chromosome identifier
            start, end = map(int, parts[-2:])
            if start <= 5000 or end >= len(genome_sequences[chromosome]) - 5000:
                sequence = genome_sequences[chromosome][start:end]
                out_f.write(f"{numt_id},{chromosome},{sequence}\n")

if __name__ == "__main__":
    random_seq_file = r"/home/john2788/gray_whales2/randomsequence_comparison.txt"
    genome_file = r"/home/john2788/gray_whales2/GCA_028021215.1_mEscRob2.pri_genomic.fna"
    output_file = r"sequences_in_boundary.csv"
    extract_sequences_in_boundary(random_seq_file, genome_file, output_file)
