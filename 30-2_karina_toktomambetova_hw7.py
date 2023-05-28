# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


# 2. В БД создать таблицу products
def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

    # 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров


def insert_products(conn, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# 8. Добавить функцию, которая меняет количество товара по id
def replacement_quantity(conn, id, quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (quantity, id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


# 9. Добавить функцию, которая меняет цену товара по id
def replacement_price(conn, id, price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price, id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


# 10. Добавить функцию, которая удаляет товар по id
def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

# 12. Добавить функцию, которая бы выбирала из БД товары которые дешевле 100 сомов и
# количество которых больше чем 5 и распечатывала бы их в консоли
def select_products(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


#13. Добавить функцию, которая бы искала в БД товары по названию
# (Например: искомое слово “мыло”, должны соответствовать поиску товары с названием -
# “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)
def select_products_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word.lower() + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


# 3. В таблицу добавить поле id -
# первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов,
# поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых
# 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity целочисленного типа данных, поле не должно быть пустым
# (NOT NULL) значением по-умолчанию поля должно быть 0
database_name = 'hw.db'
connection = create_connection(database_name)

create_products_table_sql = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) DEFAULT 0.0,
quantity TEXT NOT NULL
)
'''

if connection is not None:
    print('Successfully connected!')
    create_table(connection, create_products_table_sql)


    insert_products(connection, ("Зубная щётка", 123.25, 150))
    insert_products(connection, ("Зубная паста", 200.33, 233))
    insert_products(connection, ("Мыло банное", 60.22, 75))
    insert_products(connection, ("Мыло жидкое", 125, 50))
    insert_products(connection, ("Детское мыло", 75, 95))
    insert_products(connection, ("Порошок для разноцветной одежды 3 кг", 500.68, 35))
    insert_products(connection, ("Порошок для черно-белой одежды 1 кг", 236, 53))
    insert_products(connection, ("Комплект кухонных полотенец", 156, 43))
    insert_products(connection, ("Упаковка салфеток", 130.25, 70))
    insert_products(connection, ("Пакеты с ручкой 100 шт", 200.87, 68))
    insert_products(connection, ("Пакеты без ручки", 180.32, 80))
    insert_products(connection, ("Средство для мытья посуды", 120.22, 15))
    insert_products(connection, ("Чистящее средство", 90, 25))
    insert_products(connection, ("Средство для устранения засоров", 92, 36))
    insert_products(connection, ("Мыльница", 40.89, 92))

    # Протестировать каждую написанную функцию
    replacement_quantity(connection, 100, 6)
    replacement_price(connection, 300, 7)
    delete_product(connection, 8)
    select_all_products(connection)
    select_products(connection)
    select_products_by_word(connection, "зубная")
    connection.close()
