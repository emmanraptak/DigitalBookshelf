from reading_status import ReadingStatus

class Book():
    """Basic book class"""
    
    def __init__(self, title: str, isbn: int, status: ReadingStatus):
        self._title = title
        self._isbn = isbn
        self._status = status

    def get_title(self):
        return self._title

    def get_isbn(self):
        return self._isbn

    def get_status(self):
        return self._status