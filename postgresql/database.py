import sqlite3

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR,
                    surname VARCHAR,
                    age SMALLINT
                )''')

users_data = [
    ('John', 'Doe', 25),
    ('Jane', 'Smith', 30)
]

cursor.executemany('INSERT INTO users (name, surname, age) VALUES (?, ?, ?)', users_data)

conn.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
