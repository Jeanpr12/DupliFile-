
# File Duplication Checker

## Overview

The File Duplication Checker is a Python script that helps you identify duplicate files within a specified directory. It compares the contents of files to determine if there are any duplicates based on their byte sequences. This script can be useful for organizing your files and reclaiming disk space by removing redundant copies.

## Features

- Scan a specified directory (and its subdirectories) for duplicate files.
- Compare file contents to identify duplicates based on byte sequences.
- Display a list of duplicate files found.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/your-username/file-duplication-checker.git
    ```

2. **Navigate to the Directory**: Change into the directory where the script is located:

    ```bash
    cd file-duplication-checker
    ```

3. **Run the Script**: Execute the script and specify the directory you want to scan for duplicate files:

    ```bash
    python file_duplication_checker.py /path/to/directory
    ```

    Replace `/path/to/directory` with the path to the directory you want to search for duplicates.

4. **View Results**: The script will display a list of duplicate files found in the specified directory.

## Requirements

- Python 3.x

