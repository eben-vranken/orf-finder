def print_codons(codons: dict[str, list]):
    print(f"Found %d start codons" % len(codons["start"]))
    for i, _ in enumerate(codons["start"]):
        print(i, ":", codons["start"][i])

    print(f"Found %d stop codons" % len(codons["stop"]))
    for i, _ in enumerate(codons["stop"]):
        print(i, ":", codons["stop"][i])