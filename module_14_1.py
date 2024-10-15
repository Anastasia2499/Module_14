import sqlite3

connetion = sqlite3.connect('not_telegram.db')
cursor = connetion.cursor()
cursor.execute('''
 CREATE TABLE IF NOT EXISTS Users(
 id INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
 email TEXT NOT NULL,
 age INTEGER,
 balance INTEGER NOT NULL
 )
''')
#
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

# for i in range(1, 11):
#     if i % 2 != 0:
#         cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))
#
# a = 1
# while a <= 10:
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{a}',))
#     a += 3
#
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connetion.commit()
connetion.close()