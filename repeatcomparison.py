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
                chromosome = None
                while chromosome is None:
                    # Choose a random chromosome
                    chromosome = random.choice(list(genome_sequences.keys()))
                    # Ensure start and end locations are not within the first or last 5000 characters
                    seq_length = len(genome_sequences[chromosome])
                    if seq_length <= 10000:
                        chromosome = None  # Retry choosing chromosome
                    else:
                        # Choose random start position within chromosome boundaries
                        start_range = max(5000, len(genome_sequences[chromosome]) - 5000 - numt_length)
                        start = random.randint(5000, start_range)
                        end = start + numt_length
                        out_f.write(f"{numt_id},{chromosome},{start},{end}\n")

if __name__ == "__main__":
    genome_file = r"/scratch/negishi/allen715/shared/graywhale_numts/repeatmasker/gray_whales2/GCA_028021215.1_mEscRob2.pri_genomic.fna"
    numt_file = r"/scratch/negishi/allen715/shared/graywhale_numts/repeatmasker/gray_whales2/NUMTlength.csv"
    output_file = r"/scratch/negishi/allen715/shared/graywhale_numts/repeatmasker/gray_whales2/randomsequence_comparison.txt"
    
    generate_random_sequences(genome_file, numt_file, output_file)
