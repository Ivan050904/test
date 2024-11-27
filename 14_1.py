import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER       
)
''')

for i in range(10):
    cursor.execute(
        "INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)",
        (f"user{i}", f"example{i}@gmail.com", i * 10+10, 1000)
    )
cursor.execute("UPDATE Users set balance =? WHERE id%2 != 0 ",(500,))
cursor.execute("DELETE FROM Users WHERE id%3 == 1")
cursor.execute("SELECT * FROM Users WHERE age!=60")
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
