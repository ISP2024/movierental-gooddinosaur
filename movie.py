from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str) -> bool:
        """Check if the movie matches the given genre."""
        return genre.lower() in (g.lower() for g in self.genre)

    def __str__(self) -> str:
        """Return the string representation of the movie."""
        return f"{self.title} ({self.year})"
