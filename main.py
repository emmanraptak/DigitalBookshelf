import sqlite3

from pathlib import Path

PATH_TO_DB = Path("./data/digital_bookshelf.db")

def connect_to_database(path_to_db: Path) -> sqlite3.Connection:

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

def close_database_connection(connection: sqlite3.Connection) -> None:
        print("Attemping to close connection to the database...")
        cursor = connection.cursor
        if cursor is not None:
            cursor.close()

        connection.close()
        print("Connection to database succesfully closed!")

if __name__ == "__main__":
    connection = connect_to_database(path_to_db=PATH_TO_DB)
    if connection is not None:
        close_database_connection(connection=connection)