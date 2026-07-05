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

    i = 0
    n = len(file)
    codon_matching = False
    indexes = []
    while i < n - 2:
        codon = file[i:i+3]
        if not codon_matching:
            if codon == "ATG":
                codon_matching = True
                start = i
                i += 3
                continue
            i += 1
        else:
            if codon in ("TAA", "TAG", "TGA"):
                codon_matching = False
                indexes.append([start, i])
            i += 3

    print(indexes)