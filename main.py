import sqlite3
from pathlib import Path

from src.book import Book
from src.reading_status import ReadingStatus

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
        isbn INTEGER NOT NULL,
        status TEXT CHECK(status IN ('TBR', 'READING', 'READ', 'DNF'))
        );
        """
    )

    connection.commit()

def add_book(connection: sqlite3.Connection, book: Book) -> None:

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO BOOKS (title, isbn, status) VALUES (?, ?, ?)",
        (book.title, book.isbn10, book.status)
    )
    
    cursor.execute("SELECT * FROM BOOKS")
    print(cursor.fetchall())

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
        book = Book(
            title="Animal Farm",
            author="George Orwell",
            year_published="1945",
            isbn10=1956861378,
            isbn13=9781956861372,
            status=str(ReadingStatus.READ.value)
        )
        add_book(connection, book)
        
        close_database_connection(connection)