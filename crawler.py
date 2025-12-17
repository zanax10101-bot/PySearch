# A file crawler using os.scandir

import os

path = "." # Current directory
target_name = "crawler" # Keyword to search for

def search_directory(path, target_name):
    '''
    Use os.scandir to scan entire directory base on the path. 

    Args:
        path (string): the file path that user sets
        target_name (string): the name of the file that user wants to search for

    Returns:
        string: the path of the file that user wants to search for
    '''
    print(f"Scanning directory: {path} for the keyword: {target_name}")

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                if target_name.lower() in entry.name.lower():
                    print(f"Found the file with the keyword: {target_name} \
                    in {entry.name} at {entry.path}\n")
                    return entry.path
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
        return None

if __name__ == "__main__":
    path = input("Enter the path to search for the keyword: ")
    target_name = input("Enter the keyword to search for: ")
    result = search_directory(path, target_name)
    if result:
        print(f"Found the file with the keyword: {target_name} \
        in {result} at {result}\n")
    else:
        print(f"No file found with the keyword: {target_name}")