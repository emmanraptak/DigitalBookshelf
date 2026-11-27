from .reading_status import ReadingStatus


class Book:
    """Basic book class"""
    
    def __init__(self, title: str, author: str, isbn10: int, isbn13: int, year_published: int, status: ReadingStatus):
        self._title = title
        self._author = author
        self._isbn10 = isbn10
        self._isbn13 = isbn13
        self._year_published = year_published
        self._status = status

    def __str__(self):
        return f"{self.title} by {self.author}, published {self.year_published}."

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn10(self):
        return self._isbn10

    @property
    def isbn13(self):
        return self._isbn13

    @property
    def year_published(self):
        return self._year_published

    @property
    def status(self):
        return self._status