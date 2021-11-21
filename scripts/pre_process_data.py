import re
import nltk
from pathlib import Path

nltk.download('punkt')

OUTPUT_PATH = 'ngrams-per-file.txt'


def process_files(directory):
    with open(OUTPUT_PATH, 'w+') as f:
        f.write('')
    files = Path(directory).glob('*')
    for file in files:
        with open(file) as f:
            lines = f.read()
            sentences = _keep_letters_and_numbers(nltk.tokenize.sent_tokenize(lines))
            processed_sentences = _convert_to_lower_case(sentences)
            with open(OUTPUT_PATH, 'a') as output_file:
                output_file.write(f'Processing {file} ...\n')
                _calculate_ngrams(processed_sentences, output_file)


def _keep_letters_and_numbers(texts):
    for i, text in enumerate(texts):
        texts[i] = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return texts


def _convert_to_lower_case(texts):
    for i, text in enumerate(texts):
        texts[i] = text.lower()
    return texts


def _calculate_ngrams(sentences, file):
    for sentence in sentences:
        count = 1
        while count <= 10:
            file.write(f'n = {count}\n')
            tokens = [token for token in sentence.split(" ") if token != ""]
            ngrams = list(nltk.ngrams(tokens, count))
            processed_ngrams = []
            for item in ngrams:
                processed_ngrams.append(' '.join(item))
            file.write(f'{processed_ngrams}\n')
            count += 1
