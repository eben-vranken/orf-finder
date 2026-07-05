import reader
from argparse import ArgumentParser

def parse_args():
    args = ArgumentParser()

    args.add_argument("file", help="The location of the file to be parsed.")

    return args.parse_args()

if __name__ == "__main__":
    args = parse_args()

    sequences = reader.parse_fasta(args.file)

    print(sequences)