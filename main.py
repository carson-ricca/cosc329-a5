from pathlib import Path

from scripts import process_files, calculate_set_containment

DIRECTORY = Path('data')
N_GRAMS_FILE = Path('processed')
CSV_OUTPUT = Path('cvals.csv')

if __name__ == "__main__":
    process_files(DIRECTORY)
    calculate_set_containment(N_GRAMS_FILE, DIRECTORY, CSV_OUTPUT)
