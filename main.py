from pathlib import Path

from scripts import process_files

DIRECTORY = Path('data')
if __name__ == "__main__":
    process_files(DIRECTORY)
