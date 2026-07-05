import reader, formatter
from argparse import ArgumentParser

def parse_args():
    args = ArgumentParser()

    args.add_argument("file", help="The location of the file to be parsed.")
    args.add_argument(
        "--codons",
        action="store_true",
        help="Find and report the positions of all start (ATG) and stop (TAA, TAG, TGA) codons."
    )

    args.add_argument(
        "--orf",
        action="store_true",
        help="Identify open reading frames (ORFs) by pairing start codons with in-frame stop codons."
    )

    return args.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    if args.orf:
        sequences = reader.parse_orf(args.file)
        print(sequences)

    if args.codons:
        codons = reader.parse_codons(args.file)
        formatter.print_codons(codons)