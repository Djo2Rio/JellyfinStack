import os
from src.scrapper.french_movie import is_french_film
from src.tools.tools import *

def find_movies_with_no_subtitles(directory):
    """
    Searches for movies in the specified directory that do not have subtitles available.

    Args:
        directory (str): The path to the directory containing the movies.

    Returns:
        list: A list of movie filenames that do not have subtitles available.
    """
    subtitle_extensions = ['.srt', '.fre.srt', '.en.srt']

    # Get the list of files in the directory
    movies = os.listdir(directory)

    movie_with_missing_subtitles_added = []
    for movie in movies:

        if movie.endswith(('.mp4', '.avi', '.mkv')):
            base_name, _ = os.path.splitext(movie)

            subtitles_found = any(os.path.exists(os.path.join(directory, f"{base_name}{ext}")) for ext in subtitle_extensions)

            if not subtitles_found:
                movie_name, year = extract_name_and_year(title=base_name)
                if is_french_film(movie_name, year):
                    print("Français")
                else:
                    # TODO
                    # Extract subtiltes from the movie
                    # If no subtitles to extract, extract audio
                    # Translate
                    print("Pas français")
                    movie_with_missing_subtitles_added.append(movie)
                

    return movie_with_missing_subtitles_added