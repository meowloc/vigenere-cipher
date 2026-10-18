import argparse
import json
from collections import Counter
from pathlib import Path
from vigenere.alphabets import ALPHABETS

def main():
    parser = argparse.ArgumentParser(description='Build frequency table')
    parser.add_argument('input', type=Path, help='Path to input file')
    parser.add_argument('-o', '--output', type=Path, help='Path to output file (default: data/<lang>_freq.json)')
    parser.add_argument('-l', '--language', default='ru', choices=list(ALPHABETS), help='Alphabet language')
    parser.add_argument('-f', '--force', action='store_true', help='Force overwrite')
    args = parser.parse_args()

    alphabet = ALPHABETS[args.language]
    output = args.output or Path('data') / f'{args.language}_freq.json'

    if output.exists() and not args.force:
        parser.error(f'{output} already exists, use --force to overwrite')

    text = args.input.read_text(encoding='utf-8').lower().replace('ё', 'е')
    counts = Counter(ch for ch in text if ch in alphabet)
    total = sum(counts.values())
    if total == 0:
        parser.error(f'no letters of the "{args.language}" alphabet found in {args.input}')

    freq = {ch: counts[ch] / total for ch in alphabet}

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(freq, ensure_ascii=False, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()