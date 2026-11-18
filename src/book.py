class Book():
    """Basic book class"""
    
    def __init__(self, title: str, isbn: str):
        self._title = title
        self._isbn = isbn

    def get_title(self):
        return self._title

    def get_isbn(self):
        return self._isbn