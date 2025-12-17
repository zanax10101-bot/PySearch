# A file crawler using os.scandir
# Currently it's very basic and find one file with the keyword in the directory.
# Potential TODOS
"""
- [x] Find all files with the keyword in the directory
- [ ] Implement SQ Lite database to store the search results
- [ ] Improve the search algorithm to find the keyword in the file
- [ ] Improve the terminal CLI interface
"""

import os

def search_directory(path, target_name):
    """
    Use os.scandir to scan entire directory base on the path.

    Args:
        path (string): the file path that user sets
        target_name (string): the name of the file that user wants to search for

    Returns:
        none
    """
    matched_files = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                if target_name.lower() in entry.name.lower():
                    matched_files.append([entry.name, entry.path])
            elif entry.is_dir():
                # This fixes the issue with recursive search
                child_matched_files = search_directory(entry.path, target_name)
                matched_files.extend(child_matched_files)
    return matched_files

if __name__ == "__main__":
    path = input("Enter the path to search for the keyword: ").lower()
    target_name = input("Enter the keyword to search for: ").lower()
    result = search_directory(path, target_name)
    print(f"Found {len(result)} matching file(s).")