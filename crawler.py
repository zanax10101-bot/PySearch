# A file crawler using os.scandir

import os

path = "." # Current directory
target_name = "crawler" # 

def search_directory(path, target_name):
    '''
    Use os.scandir to scan entire directory base on the path. 

    Args:
        path (string): the file path that user sets
        target_name (string): the name of the file that user wants to search for

    Returns:
        none
    '''
    print(f"Scanning directory: {path}")

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                if target_name.lower() in entry.name.lower():
                    print(f"Found the file with the keyword: {target_name}: {entry.name}, location: {entry.path}")
            elif entry.is_dir():
                try:
                    search_directory(entry.path, target_name)
                except PermissionError:
                    print(f"Permission denied: {entry.path}")
                except FileNotFoundError:
                    print(f"File not found: {entry.path}")
                except NotADirectoryError:
                    print(f"Not a directory: {entry.path}")
                except Exception as e:
                    print(f"An error occurred: {e}")

search_directory(path, target_name)
