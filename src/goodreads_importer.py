from pathlib import Path

import pandas as pd

from .book import Book

# These should align with the columns in the SQL table
DATA_TO_KEEP = ['Title', 'Author', 'ISBN', 'ISBN13', 'Original Publication Year', 'Bookshelves']

def convert_gr_export(path_to_export: Path) -> list[Book]:
    """
    Converts the exported goodreads csv containing book data into a
    list of Book objects.

    Args:
        path_to_export (Path): path to the csv export file.

    Returns:
        list[Book]: List of Book objects constructed from the export.
    """
    
    df_raw = pd.read_csv(path_to_export)
    books_raw = df_raw[DATA_TO_KEEP].to_dict('records')

    books = [_convert_data_to_book(book_info) for book_info in books_raw]
    return books

def _convert_data_to_book(book_info: dict) -> Book:
    """
    Converts a dict containing the attributes of a book into a Book object.

    Args:
        book_info (list): attributes of a book.

    Returns:
        Book: Object containing the attributes of the book.
    """

    book = Book(
        title=book_info['Title'],
        author=book_info['Author'],
        isbn10=book_info['ISBN'],
        isbn13=book_info['ISBN13'],
        year_published=book_info['Original Publication Year'],
        status=None
        )

    return book
