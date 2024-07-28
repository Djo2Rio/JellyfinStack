import os
import re
import argparse
from src.movie_subtitle import find_movies_with_no_subtitles


def main():
    parser = argparse.ArgumentParser(description='Counts the number of subtitle files missing from a directory.')
    parser.add_argument('directory', help='Path to the directory containing the files to be scaned.')

    args = parser.parse_args()
    directory = args.directory

    # Check if the specified directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        return
    print(find_movies_with_no_subtitles(directory))

if __name__ == "__main__":
    main()