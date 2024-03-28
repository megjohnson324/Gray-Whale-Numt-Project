#!/bin/bash
#SBATCH --job-name=repeatmodelergff
#SBATCH -A highmem
#SBATCH -N 1
#SBATCH -n 32
#SBATCH -t 1-00:00:00
#SBATCH --error=test.err
#SBATCH --output=test.out
#SBATCH --mail-type=START,END,FAIL
#SBATCH --mail-user=john2788@purdue.edu


# Input file
input_file="consensi.fa.classified"

# Output GFF file
output_file="repeatmodeleroutput.gff"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: Input file '$input_file' not found."
    exit 1
fi

# Process the input file and generate the GFF file
awk -F '[#_(),= ]' 'BEGIN {OFS="\t"} {
    if ($1 ~ /^>/) {
        family = type = ""
        for (i = 2; i <= NF; i++) {
            if ($i == "family" || $i == "Type") {
                family = $(i+1)
            }
            if ($i ~ /^family-/) {
                type_start = index($i, "-") + 1
                type = substr($i, type_start)
            }
        }
        start = $9
        end = $10
        seq_name = gensub(">", "", "g", $1)

        # Print GFF format
        print seq_name, type, start, end, ".", ".", ".", "ID=" seq_name ";Family=" family ";Type=" type
    }
}' "$input_file" > "$output_file"
