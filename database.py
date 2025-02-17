import sqlite3

DB_NAME = "meals.db"

def create_connection():
    """Creates a database connection and returns a cursor."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    """Creates tables if they don’t exist."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        calories INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# Run table creation when script is executed
if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully!")
