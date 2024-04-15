import sqlite3

DATABASE = 'waitlist.db'

def create_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_email(email):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO emails (email) VALUES (?)', (email,))
    conn.commit()
    conn.close()

def get_emails():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM emails')
    emails = [row[0] for row in cursor.fetchall()]
    conn.close()
    return emails

if __name__ == '__main__':
    create_tables()  # Call create_tables() only if the script is executed directly
