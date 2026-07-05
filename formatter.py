def print_codons(codons: dict[str, list]):
    for i, _ in enumerate(codons["start"]):
        print(i, ":", codons["start"][i])

    for i, _ in enumerate(codons["stop"]):
        print(i, ":", codons["stop"][i])

    print(f"Found %d start codons" % len(codons["start"]))
    print(f"Found %d stop codons" % len(codons["stop"]))