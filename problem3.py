import os

def print_directory_contents(path):
    try:
        entries = os.listdir(path)   # returns names in the directory
    except FileNotFoundError:
        print(f"Error: Directory not found: {path}")
        return
    except PermissionError:
        print(f"Error: Permission denied: {path}")
        return

    print(f"Contents of directory '{path}':")
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    # You can change this to any directory you want
    directory_path = '/New folder'  # current directory
    print_directory_contents(directory_path)
