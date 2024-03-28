def parse_bed_file(bed_file):
    sequences = []
    with open(bed_file, 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            sequence = {'chromosome': fields[0], 'start': int(fields[1]), 'end': int(fields[2])}
            sequences.append(sequence)
    return sequences

def parse_repeatmasker_file(repeatmasker_file):
    repeats = []
    with open(repeatmasker_file, 'r') as f:
        header_lines_skipped = False
        for line in f:
            if not header_lines_skipped:
                if line.startswith('SW') or line.startswith('score'):
                    header_lines_skipped = True
                continue
            
            if line.strip():  # Skip empty lines
                fields = line.strip().split()  # Split by any whitespace
                if len(fields) >= 15:  # Adjust field count as per your file format
                    repeat = {'query': fields[4], 'repeat_start': int(fields[5]), 'repeat_end': int(fields[6]), 'repeat_class/family': fields[10]}
                    repeats.append(repeat)
                else:
                    print("Warning: Skipping line due to insufficient fields:", line.strip())
    return repeats

def find_nearby_repeats(sequences, repeats, threshold=5000):
    nearby_repeats = []
    for seq in sequences:
        for repeat in repeats:
            if (repeat['repeat_start'] - seq['start'] <= threshold and repeat['repeat_start'] - seq['start'] >= 0) \
                or (seq['end'] - repeat['repeat_end'] <= threshold and seq['end'] - repeat['repeat_end'] >= 0):
                nearby_repeats.append({'sequence_of_interest': seq['chromosome'], 
                                       'repeat_start': repeat['repeat_start'], 
                                       'repeat_end': repeat['repeat_end'], 
                                       'repeat_class/family': repeat['repeat_class/family']})
    return nearby_repeats

def write_comparison_file(nearby_repeats, output_file):
    with open(output_file, 'w') as f:
        f.write("sequence\trepeat_start\trepeat_end\trepeat_class/family\n")
        for repeat in nearby_repeats:
            f.write("{}\t{}\t{}\t{}\n".format(repeat['sequence'], repeat['repeat_start'], repeat['repeat_end'], repeat['repeat_class/family']))

def main():
    bed_file = "sequences_of_interest_fixed.bed"
    repeatmasker_file = "GCA_028021215.1_mEscRob2.pri_genomic.fna.out"
    comparison_file = "comparison.txt"
    
    sequences = parse_bed_file(bed_file)
    repeats = parse_repeatmasker_file(repeatmasker_file)
    nearby_repeats = find_nearby_repeats(sequences, repeats)
    
    # Modify the sequence column to represent line number in bed file
    for i, repeat in enumerate(nearby_repeats):
        repeat['sequence'] = i + 1
        
    write_comparison_file(nearby_repeats, comparison_file)

if __name__ == "__main__":
    main()

# def write_comparison_file(nearby_repeats, output_file):
#     with open(output_file, 'w') as f:
#         f.write("sequence_of_interest\trepeat_start\trepeat_end\trepeat_class/family\n")
#         for repeat in nearby_repeats:
#             f.write("{}\t{}\t{}\t{}\n".format(repeat['sequence_of_interest'], repeat['repeat_start'], repeat['repeat_end'], repeat['repeat_class/family']))
# 
# def main():
#     bed_file = "sequences_of_interest_fixed.bed"
#     #repeatmasker_file = "GCA_028021215.1_mEscRob2.pri_genomic.fna.out"
#     repeatmasker_file = "repeatmasker_GCA_028021215.1_mEscRob2.pri_genomic.fna.out"
#     comparison_file = "comparison.txt"
#     
#     sequences = parse_bed_file(bed_file)
#     repeats = parse_repeatmasker_file(repeatmasker_file)
#     print("Number of sequences:", len(sequences))
#     print("Number of repeats:", len(repeats))
#     
#     nearby_repeats = find_nearby_repeats(sequences, repeats)
#     print("Number of nearby repeats:", len(nearby_repeats))
#     
#     write_comparison_file(nearby_repeats, comparison_file)
# 
# if __name__ == "__main__":
#     main()
