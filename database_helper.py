import sqlite3

def create_connection():
    conn = sqlite3.connect('messages.db')
    return conn

def create_table():
    conn = create_connection()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        """)

def save_message(content):
    conn = create_connection()
    with conn:
        conn.execute("INSERT INTO messages (content) VALUES (?)", (content,))
        
def get_last_message():
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT content FROM messages ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        return row[0] if row else None

# Create the table when the script is first run
create_table()
