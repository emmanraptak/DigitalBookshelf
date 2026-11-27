import sqlite3
from pathlib import Path

from src.book import Book
from src.goodreads_importer import convert_gr_export

PATH_TO_DB = Path("./data/bookshelf.db")

def connect_to_database() -> sqlite3.Connection:

    connection = None

    if not PATH_TO_DB.exists():
        Path(PATH_TO_DB).parent.mkdir(parents=True, exist_ok=True)

    try:
        print("Attempting to connect to the database...")
        connection = sqlite3.connect(str(PATH_TO_DB))

    except sqlite3.Error as error:    
        print("Error connecting to database:", error)

    finally: 
        print("Database connected to successfully!")
    
    return connection

def create_books_table(connection: sqlite3.Connection) -> None:
    
    # TODO: generalise status based on user input
    # TODO: wrap this call

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS BOOKS (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        isbn10 TEXT UNIQUE,
        isbn13 TEXT UNIQUE,
        year_published INTEGER
        );
        """
    )

    connection.commit()

def add_book(connection: sqlite3.Connection, book: Book) -> None:

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO BOOKS (title, author, isbn10, isbn13, year_published) VALUES (?, ?, ?, ?, ?)",
        (book.title, book.author, book.isbn10, book.isbn13, book.year_published)
    )

def close_database_connection(connection: sqlite3.Connection) -> None:
        
        print("Attemping to close connection to the database...")
        connection.close()
        print("Connection to database succesfully closed!")

if __name__ == "__main__":
    connection = connect_to_database()
    if connection is not None:
        cursor = connection.cursor()

        create_books_table(connection)

        # Test code for now
        books = convert_gr_export(Path("goodreads_library_export.csv"))
        for book in books:
            add_book(connection, book)
        
        close_database_connection(connection)