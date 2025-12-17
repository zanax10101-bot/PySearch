# MVP implementation of a file crawler using os.scandir

import os

path = "/Users/zanax" # My home path

def scan_directory(path):
    '''
    Use os.scandir to scan entire directory base on the path. 
    Output the file names and the directory names.

    Args:
        path (string): the file path that user sets

    Returns:
        none
    '''
    print(f"Scanning directory: {path}")

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"File: {entry.name}")
            elif entry.is_dir():
                print(f"Folder: {entry.name}")

# Use the function
scan_directory(path)
