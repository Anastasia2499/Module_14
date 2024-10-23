import sqlite3


def initiate_db():
    connetion = sqlite3.connect('Products.db')
    cursor = connetion.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    connetion.commit()

    connetion = sqlite3.connect('base_user.db')
    cursor = connetion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        ''')

    connetion.commit()

# initiate_db()


def add_user(username, email, age, balance=1000):
    connetion = sqlite3.connect('base_user.db')
    cursor = connetion.cursor()
    cursor.execute("INSERT INTO Products (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'{username}', f'{email}', f'{age}', f'{balance}'))
    connetion.commit()


def is_included(username):
    connetion = sqlite3.connect('base_user.db')
    cursor = connetion.cursor()
    check_user = cursor.execute('SELECT id FROM Users WHERE username = ?', (username,))
    if check_user.fetchone():
        return True
    else:
        return False


def get_all_products():
    connetion = sqlite3.connect('Products.db')
    cursor = connetion.cursor()
    for i in range(1, 5):
        title_ = f'Продукт{i}'
        description_ = f'Описание{i}'
        price_ = i * 100
        check_price = cursor.execute('SELECT id FROM Products WHERE title = ?', (title_,))
        if check_price.fetchone() is None:
            cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f'{title_}', f'{description_}', f'{price_}'))
    price_list = cursor.execute('SELECT * FROM Products')
    message = []
    for user in price_list:
        message.append(f'Название: {user[1]} | Описание: {user[2]} | Стоимость: {user[3]} \n')
    connetion.commit()
    return message




# connetion.commit()
# connetion.close()
