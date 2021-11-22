import os
import re
import nltk
from pathlib import Path

from util import mkdir_if_not_exists

nltk.download('punkt')
PROCESSED = 'processed/'


def process_files(directory):
    """
    Process each file in the specified directory and determines the number of ngrams.
    :param directory: The directory to determine the ngrams for.
    """
    mkdir_if_not_exists(PROCESSED)
    files = Path(directory).glob('*')
    for file in files:
        with open(f'processed/processed-{os.path.basename(file)}', 'w+') as f:
            f.write('')
        with open(file) as f:
            lines = f.read()
            sentences = _keep_letters_and_numbers(nltk.tokenize.sent_tokenize(lines))
            processed_sentences = _convert_to_lower_case(sentences)
            with open(f'processed/processed-{os.path.basename(file)}', 'a') as output_file:
                output_file.write(f'Processing {file} ...\n')
                _calculate_ngrams(processed_sentences, output_file)


def _keep_letters_and_numbers(texts):
    """
    Remove all non-alphanumeric characters from strings.
    :param texts: The sentences to process.
    :return: The processed sentences.
    """
    for i, text in enumerate(texts):
        texts[i] = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return texts


def _convert_to_lower_case(texts):
    """
    Converts strings to lower-case.
    :param texts: The sentences to process.
    :return: The processed sentences.
    """
    for i, text in enumerate(texts):
        texts[i] = text.lower()
    return texts


def _calculate_ngrams(sentences, file):
    """
    Calculates the ngrams for sentences and writes them to the output file.
    :param sentences: The sentences to calculate ngrams for.
    :param file: The file to write to.
    """
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
