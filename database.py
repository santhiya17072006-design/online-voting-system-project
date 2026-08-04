import sqlite3

def create_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        mobile TEXT,
        password TEXT,
        otp TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS votes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        voter_email TEXT,
        candidate TEXT
    )
    """)

    connection.commit()
    connection.close()

create_database()
