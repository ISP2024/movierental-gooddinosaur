from datetime import datetime
from movie import Movie
from price_strategy import NEW_RELEASE, REGULAR, CHILDREN


def price_code_for_movie(movie: Movie) -> str:
    current_year = datetime.now().year
    if movie.year == current_year:
        return NEW_RELEASE
    elif any(genre.lower() == "children" or genre.lower() == "childrens" for genre in movie.genre):
        return CHILDREN
    else:
        return REGULAR
