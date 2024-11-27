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
cursor.execute("DELETE FROM Users WHERE id == 6")
cursor.execute("SELECT COUNT(*) FROM Users")
total_1 = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
total_2 = cursor.fetchone()[0]
cursor.execute("SELECT AVG(balance) FROM Users")
total_3 = cursor.fetchone()[0]
print(total_1)
print(total_2)
print(total_3)


connection.commit()
connection.close()
