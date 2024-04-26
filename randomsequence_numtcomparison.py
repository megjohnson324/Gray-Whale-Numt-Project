#This script generates 100 random sequences per NUMT and included start and end location of each NUMT. 
import random

def load_genome_sequences(genome_file):
    genome_sequences = {}
    current_chromosome = None
    with open(genome_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                current_chromosome = line.strip()
                genome_sequences[current_chromosome] = ""
            else:
                genome_sequences[current_chromosome] += line.strip()
    return genome_sequences

def generate_random_sequences(genome_file, numt_file, output_file, num_sequences=100):
    # Load NUMT lengths
    numt_lengths = {}
    with open(numt_file, 'r') as f:
        next(f)  # Skip header
        for line in f:
            numt_id, length = line.strip().split(',')
            numt_lengths[numt_id] = int(length)

    # Load genome sequences
    genome_sequences = load_genome_sequences(genome_file)

    # Generate random sequences
    with open(output_file, 'w') as out_f:
        out_f.write("NUMT_ID,Chromosome,Start,End\n")
        for numt_id, numt_length in numt_lengths.items():
            for _ in range(num_sequences):
                chromosome = random.choice(list(genome_sequences.keys()))
                seq_length = len(genome_sequences[chromosome])
                start = random.randint(0, seq_length - numt_length)
                end = start + numt_length
                out_f.write(f"{numt_id},{chromosome},{start},{end}\n")

if __name__ == "__main__":
    genome_file = r"/scratch/negishi/allen715/shared/graywhale_numts/repeatmasker/gray_whales2/GCA_028021215.1_mEscRob2.pri_genomic.fna"
    numt_file = r"/scratch/negishi/allen715/shared/graywhale_numts/repeatmasker/gray_whales2/NUMTlength.csv"
    output_file = r"/scratch/negishi/allen715/shared/graywhale_numts/repeatmasker/gray_whales2/randomsequence_comparison.txt"
    
    generate_random_sequences(genome_file, numt_file, output_file)
