def load_sequence(file_location):
    sequence_lines = []

    with open(file_location) as fp:
        for line in fp:
            cleaned_line = line.strip()

            if cleaned_line.startswith(">") or not cleaned_line:
                continue

            sequence_lines.append(cleaned_line)
    
    return "".join(sequence_lines).upper()

if __name__ == "__main__":
    file = load_sequence("test_data/zika_thailand_2006_complete.fasta")

    codon_matching = False
    indexes = []
    current_index = []
    for i, c in enumerate(file[:len(file)-2]):
        codon = file[i] + file[i+1] + file[i+2]

        if codon == "ATG" and not codon_matching:
            codon_matching = True
            current_index.append(i)
        elif (codon == "TAA" or codon == "TAG" or codon == "TGA") and codon_matching:
            codon_matching = False
            current_index.append(i)
            indexes.append(current_index)
            current_index = []
        
        if codon_matching:
            i += 2

    print(indexes)