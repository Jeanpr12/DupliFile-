import os

def find_duplicate_files(directory):
    """
    Find duplicate files in the specified directory.
    """
    files_seen = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    file_content = f.read()

                if file_content in files_seen.values():
                    duplicates.append(file_path)
                else:
                    files_seen[file] = file_content

    return duplicates

def main():
    # Specify directory to search for duplicates
    directory = '/path/to/directory'  # Change this to your desired directory
    duplicate_files = find_duplicate_files(directory)

    if duplicate_files:
        print("Duplicate files found:")
        for file_path in duplicate_files:
            print(file_path)
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()
