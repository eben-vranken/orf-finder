<h1 align="center">🧬 ORF Finder</h1>

<p align="center">
    A command-line utility to locate start and stop codons and identify open reading frames (ORFs) in DNA/RNA sequences.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI built to scan genomic sequence strings for coding structure. It reads raw FASTA-style input, locates every start and stop codon in the sequence, and pairs start codons with their nearest in-frame stop codon to report complete open reading frames.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/orf-finder.git
cd orf-finder
```

## Usage

Pass a text file containing a raw genomic sequence. By default, the tool runs in ORF mode and reports every open reading frame it finds.

```bash
python cli.py sequence.fasta
```

### Locate Individual Codons

Report the positions of every start and stop codon in the sequence using the `--codons` flag:

```bash
python cli.py sequence.fasta --codons
```

### RNA Mode

Switch the codon search to RNA bases (`AUG`, `UAA`, `UAG`, `UGA`) with the `--rna` flag:

```bash
python cli.py sequence.fasta --rna
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `file` | *Positional path string* | *Required* | Path to the input file containing raw genomic text. |
| `--orf` | *Flag* | `True` | Identifies open reading frames by pairing start codons with in-frame stop codons. |
| `--codons` | *Flag* | `False` | Finds and reports the positions of all start and stop codons individually. |
| `--rna` | *Flag* | `False` | Sets the codon search mode to RNA bases instead of DNA bases. |

## Feature Set

* **Start/Stop Codon Detection:** Scans the full sequence for `ATG` start codons and `TAA`, `TAG`, `TGA` stop codons (or their RNA equivalents).
* **Open Reading Frame Pairing:** Matches each start codon to its nearest in-frame stop codon to report complete ORFs.
* **DNA and RNA Modes:** Toggles codon matching between DNA and RNA alphabets with a single flag.
* **FASTA-Aware Parsing:** Strips header lines and stray whitespace from the input file before scanning.

## Testing

Run the automated test suite to verify parsing logic accuracy, codon frame coverage, and CLI edge-case execution pipelines:

```bash
python -m unittest discover
```

### Coverage Report

To review full execution trace line metrics:

```bash
python -m coverage run -m unittest discover
python -m coverage report -m
```

## License

MIT