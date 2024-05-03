import sqlite3


def init_db():
    """
    A function to initialize the SQLite database
    :return: The database connection object
    """
    conn = sqlite3.connect('measurements.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS conversions
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_input TEXT,
                      converted_result TEXT,
                      status TEXT,
                      error_message TEXT)''')
    conn.commit()
    return conn
