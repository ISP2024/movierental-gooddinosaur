import csv
import logging
from typing import Optional
from movie import Movie


class MovieCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance._movies = {}
            cls._instance._loaded = False
        return cls._instance

    def _load_movies(self):
        try:
            with open('movies.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for line_number, row in enumerate(reader):
                    if not row or row[0].startswith('#'):
                        continue
                    if len(row) < 3:
                        logging.error(f"Line {line_number + 1}: Unrecognized format {row}")
                        continue
                    try:
                        movie_id, title, year, *genres = row
                        year = int(year)
                        genre_list = [genre.strip() for genre in
                                      genres[0].split('|')] if genres else []
                        movie = Movie(title, year, genre_list)
                        self._movies[(title.lower(), year)] = movie
                    except ValueError as e:
                        logging.error(f"Line {line_number + 1}: {e}")
        except FileNotFoundError:
            logging.error("The movie data file was not found.")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        if not self._loaded:
            self._load_movies()
            self._loaded = True
        if year is None:
            for (stored_title, stored_year), movie in self._movies.items():
                if stored_title == title.lower():
                    return movie
        else:
            return self._movies.get((title.lower(), year))
