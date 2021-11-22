import ast
import os
import pandas as pd
from pathlib import Path


def calculate_set_containment(directory, data_directory, csv_directory):
    """
    Calculates the set containment and exports to a csv.
    :param directory: The processed data directory.
    :param data_directory: The raw data directory.
    :param csv_directory: The path for the exported csv.
    """
    files = Path(directory).glob('*')
    raw_files = Path(data_directory).glob('*')
    file_names = []
    for file in raw_files:
        file_names.append(os.path.basename(file))
    file_sets = dict()
    for file in files:
        total_ngrams = _combine_ngrams(file)
        file_sets[os.path.basename(file)] = _create_ngram_sets(total_ngrams)
    df = _write_to_csv(file_names, file_sets)
    df.to_csv(csv_directory, index=False)


def _combine_ngrams(file):
    """
    This function combines all the ngrams for a file into a single array. I.e. all ngrams for n = 1 in the specified
    file are all in the same array.
    :param file: The file to combine ngrams for.
    :return: Returns the array with all the combined ngrams.
    """
    total_ngrams = [[], [], [], [], [], [], [], [], [], []]
    with open(file, 'r') as f:
        lines = f.readlines()
        n = 0
        for line in lines:
            if 'Processing' in line:
                pass
            elif 'n = ' in line:
                for word in line.split():
                    if word.isdigit():
                        n = int(word)
            else:
                ngrams = ast.literal_eval(line)
                total_ngrams[n - 1].extend(ngrams)
    return total_ngrams


def _create_ngram_sets(file_ngrams):
    """
    This function creates a dictionary with the key being n and the value being the set of ngrams for n.
    :param file_ngrams: The combined ngrams for a file.
    :return: The dictionary with the sets of ngrams for a file.
    """
    file_ngrams_dict = dict()
    for i, ngram in enumerate(file_ngrams):
        file_ngrams_dict[i + 1] = set(ngram)
    return file_ngrams_dict


def _calculate_containment(set_a, set_b):
    """
    This function calculates the containment value given two sets.
    :param set_a: First set.
    :param set_b: Second set.
    :return: The containment value.
    """
    numerator = len(set_a.intersection(set_b))
    denominator = len(set_b)
    return numerator / denominator


def _write_to_csv(file_names, file_sets):
    """
    This function writes all containment values to a csv.
    :param file_names: An array with the file names.
    :param file_sets: The sets of the ngrams for the associated file names.
    :return:
    """
    df = pd.DataFrame(
        columns=['A', 'B', 'C_1(A, B)', 'C_2(A, B)', 'C_3(A, B)', 'C_4(A, B)', 'C_5(A, B)', 'C_6(A, B)', 'C_7(A, B)',
                 'C_8(A, B)', 'C_9(A, B)', 'C_10(A, B)'])
    count = 1
    while count <= 9:
        file_a = file_names[count - 1]
        row = []
        for key, value in file_sets.items():
            row.append(file_a)
            row.append(key.replace('processed-', ''))
            for k, v in value.items():
                row.append(_calculate_containment(file_sets[f'processed-{file_a}'].get(k), v))
            df.loc[df.shape[0]] = row
            row = []
        count += 1
    return df
