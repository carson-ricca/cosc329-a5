import re
import nltk
from pathlib import Path

nltk.download('punkt')


def process_files(directory):
    files = Path(directory).glob('*')
    for file in files:
        with open(file) as f:
            lines = f.read()
            sentences = _keep_letters_and_numbers(nltk.tokenize.sent_tokenize(lines))
            processed_sentences = _convert_to_lower_case(sentences)
            print(f'Processing {file} ...')
            _calculate_ngrams(processed_sentences)


def _keep_letters_and_numbers(texts):
    for i, text in enumerate(texts):
        texts[i] = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return texts


def _convert_to_lower_case(texts):
    for i, text in enumerate(texts):
        texts[i] = text.lower()
    return texts


def _calculate_ngrams(sentences):
    for sentence in sentences:
        count = 1
        while count <= 10:
            print(f'n = {count}')
            tokens = [token for token in sentence.split(" ") if token != ""]
            print(list(nltk.ngrams(tokens, count)))
            count += 1
