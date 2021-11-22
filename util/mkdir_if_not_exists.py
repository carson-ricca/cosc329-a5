import os


def mkdir_if_not_exists(path):
    """
    Creates a directory if it doesn't already exist.
    :param path: The path to the directory.
    """
    if not os.path.exists(path):
        os.mkdir(path)
