import sqlite3

def init_db():
    con = sqlite3.connect("jarvis.db")
    cursor = con.cursor()

    # Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS sys_command(
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        path VARCHAR(1000)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS web_command(
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        url VARCHAR(1000)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY,
        name VARCHAR(200),
        mobile_no VARCHAR(255),
        email VARCHAR(255),
        city VARCHAR(255)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS info(
        name VARCHAR(100),
        designation VARCHAR(50),
        mobileno VARCHAR(40),
        email VARCHAR(200),
        city VARCHAR(300)
    )''')

    # Insert sample data if tables are empty
    cursor.execute("SELECT COUNT(*) FROM sys_command")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO sys_command (name, path) VALUES (?, ?)", ("notepad", "notepad.exe"))
        cursor.execute("INSERT INTO sys_command (name, path) VALUES (?, ?)", ("calculator", "calc.exe"))

    cursor.execute("SELECT COUNT(*) FROM web_command")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO web_command (name, url) VALUES (?, ?)", ("youtube", "https://www.youtube.com/"))
        cursor.execute("INSERT INTO web_command (name, url) VALUES (?, ?)", ("google", "https://www.google.com/"))

    cursor.execute("SELECT COUNT(*) FROM contacts")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO contacts (name, mobile_no, email, city) VALUES (?, ?, ?, ?)", ("John Doe", "1234567890", "john@example.com", "New York"))

    con.commit()
    con.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
