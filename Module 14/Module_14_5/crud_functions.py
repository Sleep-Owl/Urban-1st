import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт {i}', f'Описание {i}', f'{i * 100}'))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance  INTEGER NOT NULL
        )
        ''')

    connection.commit()


# initiate_db()


def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    results = cursor.fetchall()
    return results


def add_user(username, email, age):
    check_new_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))

    if check_new_user.fetchone() is None:
        cursor.execute(f'''
        INSERT INTO Users (username, email, age, balance) VALUES('{username}', '{email}', '{age}', 1000) 
        ''')
    connection.commit()


def is_included(username):
    check_user = cursor.execute('SELECT username FROM Users WHERE username = ?', (username,))
    check = check_user.fetchone()

    if check is None:
        return False
    else:
        return True


connection.commit()
# connection.close()
