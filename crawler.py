# A file crawler using os.scandir
# Finds files in the given path that contains the target name.
import os

def search_directory(path: str, target_name: str) -> list[tuple[str, str]]:
    """
    Use os.scandir to scan entire directory based on the path.

    Args:
        path (string): the file path that user sets
        target_name (string): the name of the file that user wants to search for

    Returns:
        (list): a list of tuples, each tuple contains the matched filename and the path
        of the matched file.
    """
    matched_files = []
    # Handle Errors if the current directory is not accessible
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                # Handles Errors if there is weird entires, broken links, etc.
                try:
                    if entry.is_file():
                        if target_name.lower() in entry.name.lower():
                            matched_files.append((entry.name, entry.path))
                    elif entry.is_dir(follow_symlinks=False): 
                        child_matched_files = search_directory(entry.path, target_name)
                        matched_files.extend(child_matched_files)
                except Exception as e:
                    print(f"An error occurred: {e}")
        return matched_files
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
'''
def main():
    while True:
        path = input("Enter the path to search for the keyword: ")
        if path == "":
            print("Input cannot be empty.")
        elif not os.path.exists(path):
            print("Please enter a path that exists.")
        elif not os.path.isdir(path):
            print("Please enter a valid directory.")
        else:
            break
    while True:
        target_name = input("Enter the keyword to search for: ").strip()
        if target_name == "":
            print("Input cannot be empty.")
        else:
            break
    result = search_directory(path, target_name)
    print(f"Found {len(result)} matching file(s) with the keyword: {target_name}.")
    for file in result:
        print(f"MatchedFile: {file[0]} at {file[1]}")
'''