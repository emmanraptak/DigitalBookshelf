from pathlib import Path

from src import db_helpers
from src.goodreads_importer import convert_gr_export

if __name__ == "__main__":
    connection = db_helpers.connect_to_database()
    if connection is not None:
        cursor = connection.cursor()

        db_helpers.create_books_table(connection)

        # Test code for now
        books = convert_gr_export(Path("goodreads_library_export.csv"))
        for book in books:
            db_helpers.add_book(connection, book)
        
        db_helpers.close_database_connection(connection)