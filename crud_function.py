import sqlite3
connection = sqlite3.connect('products.db')
cursor = connection.cursor()

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL      
    )
    ''')

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products

def add_user(username, email, age):
    check_user = cursor.execute("SELECT * FROM Users WHERE id = ? ", (username,))

    if check_user.fetchone() is None:
        cursor.execute('''
                INSERT INTO Users (username, email, age, balance) 
                VALUES (?, ?, ?, ?)
            ''', (username, email, age, 1000))


connection.commit()

