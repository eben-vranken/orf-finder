def load_sequence(sequence_location):
    sequence_lines = []

    with open(sequence_location) as fp:
        for line in fp:
            cleaned_line = line.strip()

            if cleaned_line.startswith(">") or not cleaned_line:
                continue

            sequence_lines.append(cleaned_line)
    
    return "".join(sequence_lines).upper()

def parse_orf(sequence_location):
    sequence = load_sequence(sequence_location)

    i = 0
    n = len(sequence)
    codon_matching = False
    indexes = []
    while i < n - 2:
        codon = sequence[i:i+3]
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

    return indexes

def parse_codons(sequence_location):
    sequence = load_sequence(sequence_location)

    i = 0
    n = len(sequence)
    indexes = {
        "start": [],
        "stop": [],
    }
    while i < n - 2:
        codon = sequence[i:i+3]
        if codon == "ATG":
            indexes["start"].append(i)   

        if codon in ("TAA", "TAG", "TGA"):
             indexes["stop"].append([i, codon])   
        
        i += 3

    return indexes