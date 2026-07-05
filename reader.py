def load_sequence(sequence_location):
    sequence_lines = []

    with open(sequence_location) as fp:
        for line in fp:
            cleaned_line = line.strip()

            if cleaned_line.startswith(">") or not cleaned_line:
                continue

            sequence_lines.append(cleaned_line)
    
    return "".join(sequence_lines).upper()

def parse_orf(sequence_location, rna):
    sequence = load_sequence(sequence_location)

    i = 0
    n = len(sequence)
    codon_matching = False
    indexes = []
    while i < n - 2:
        codon = sequence[i:i+3]
        if not codon_matching:
            if (not rna and codon == "ATG") or (rna and codon == "AUG"):
                codon_matching = True
                start = i
                i += 3
                continue
            i += 1
        else:
            if (not rna and codon in ("TAA", "TAG", "TGA")) or (rna and codon in ("UAA", "UAG", "UGA")):
                codon_matching = False
                indexes.append([start, i])
            i += 3

    return indexes

def parse_codons(sequence_location, rna):
    sequence = load_sequence(sequence_location)

    i = 0
    n = len(sequence)
    indexes = {
        "start": [],
        "stop": [],
    }
    while i < n - 2:
        codon = sequence[i:i+3]
        if (not rna and codon == "ATG") or (rna and codon == "AUG"):
            indexes["start"].append(i)   

        if (not rna and codon in ("TAA", "TAG", "TGA")) or (rna and codon in ("UAA", "UAG", "UGA")):
             indexes["stop"].append([i, codon])   
        
        i += 3

    return indexes