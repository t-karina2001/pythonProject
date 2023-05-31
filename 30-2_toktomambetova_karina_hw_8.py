import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_countries(conn, country):
    try:
        sql = '''INSERT INTO countries (title) 
        VALUES (?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (country,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_cities(conn, city, area, country_id):
    try:
        sql = '''INSERT INTO cities (title, area, country_id) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, (city, area, country_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_employees(conn, first_name, last_name, city_id):
    try:
        sql = '''INSERT INTO employees (first_name, last_name, city_id) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, (first_name, last_name, city_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_cities(conn):
    try:
        sql = '''SELECT title FROM cities'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_employees(conn, city_id):
    try:
        sql = '''SELECT employees.first_name, employees.last_name, countries.title AS country, cities.title AS city
        FROM employees
        INNER JOIN cities ON employees.city_id = cities.id
        INNER JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (city_id,))
        employees = cursor.fetchall()
        return employees
    except sqlite3.Error as e:
        print(e)
        return []


database_name = 'homework.db'
connection = create_connection(database_name)

# 1. Создать таблицу countries (страны)
# c колонками id первичный ключ автоинкрементируемый и колонка title с текстовым не пустым названием страны.
create_countries_table_sql = '''
CREATE TABLE countries (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
title VARCHAR(200) NOT NULL
)
'''

# 3. Добавить таблицу cities (города) c колонками id первичный ключ автоинкрементируемый,
# колонка title с текстовым не пустым названием города и колонка area площадь города не
# целочисленного типа данных со значением по умолчанием 0,
# а также колонка country_id с внешним ключом на таблицу countries.
create_cities_table_sql = '''
CREATE TABLE IF NOT EXISTS cities (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(200) NOT NULL,
area REAL DEFAULT 0,
country_id INTEGER,
FOREIGN KEY (country_id) REFERENCES countries (id)
)'''

# 5. Создать таблицу employees (сотрудники) c колонками id первичный ключ автоинкрементируемый,
# колонка first_name (имя) с текстовым не пустым значением,
# колонка last_name (фамилия) с текстовым не пустым значением,
# а также колонка city_id с внешним ключом на таблицу cities.
create_employees_table_sql = '''
CREATE TABLE IF NOT EXISTS employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(200) NOT NULL,
last_name VARCHAR(200) NOT NULL,
city_id INTEGER,
FOREIGN KEY (city_id) REFERENCES cities (id)
)'''

if connection is not None:
    print('Successfully connected!')
    create_table(connection, create_countries_table_sql)
    create_table(connection, create_cities_table_sql)
    create_table(connection, create_employees_table_sql)

    # 2. Добавить 3 записи в таблицу countries
    insert_countries(connection, ('Кыргызстан'))
    insert_countries(connection, ('Америка'))
    insert_countries(connection, ('Корея'))

    # 4. Добавить 7 городов различных стран
    insert_cities(connection, 'Бишкек', 156.45, 1)
    insert_cities(connection, 'Каракол', 452.56, 1)
    insert_cities(connection, 'Балыкчы', 930.95, 1)
    insert_cities(connection, 'Нью-Йорк', 756.84, 2)
    insert_cities(connection, 'Сеул', 456.20, 3)
    insert_cities(connection, 'Вашингтон', 987.65, 2)
    insert_cities(connection, 'Пусан', 984, 3)

    # 6. Добавить 15 сотрудников проживающих в разных городах.
    insert_employees(connection, 'Алмаш', 'Абдраимова', 1)
    insert_employees(connection, 'Акылай', 'Мурзаканова', 2)
    insert_employees(connection, 'Айдар', 'Орозакунов', 3)
    insert_employees(connection, 'Нурлан', 'Шамшиев', 4)
    insert_employees(connection, 'Сайкал', 'Нусубалиева', 5)
    insert_employees(connection, 'Индира', 'Алымкожоева', 6)
    insert_employees(connection, 'Нургуль', 'Уланова', 7)
    insert_employees(connection, 'Омурбек', 'Исманов', 6)
    insert_employees(connection, 'Азат', 'Нурдинов', 5)
    insert_employees(connection, 'Азамат', 'Кудайбергенов', 4)
    insert_employees(connection, 'Мээрим', 'Бакытбекова', 3)
    insert_employees(connection, 'Сезим', 'Жылдызбекова', 2)
    insert_employees(connection, 'Милана', 'Исхазова', 1)
    insert_employees(connection, 'Азалия', 'Эрикова', 2)
    insert_employees(connection, 'Динара', 'Айтахунова', 3)

    connection.close()


# 8. Ниже фразы программа должна распечатывать список городов из вашей базы данных следующим образом
# Бишкек
# Ош
# Берлин
# Пекин
# и тд…
def cities_list(conn):
    cities = select_cities(conn)
    print('Список городов: ')
    for city in cities:
        print(city[0])


# 9. После ввода определенного id города программа должна найти
# всех сотрудников из вашей базы данных проживающих в городе выбранного пользователем и отобразить информацию
# о них в консоли (Имя, фамилия, страна и город проживания)
def search_employees(conn, city_id):
    employees = select_employees(conn, city_id)
    print('Список сотрудников, проживающих в данном городе: ')
    for employee in employees:
        print(f'Имя: {employee[0]}, Фамилия: {employee[1]}, Страна: {employee[2]}, Город проживания: {employee[3]}')

        # 7. Написать программу в Python, которая при запуске бы отображала фразу
        # “Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже,
        # для выхода из программы введите 0:”


def run_program():
    database_name = 'homework.db'
    connection = create_connection(database_name)

    if connection is not None:
        print('Вы можете отобразить список сотрудников по выбранному id города'
              ' из перечня городов ниже, для выхода из программы введите 0:')
        cities_list(connection)

        while True:
            city_id = int(input('Введите id города: '))
            if city_id == 0:
                break

        select_employees(connection, city_id)

    connection.close()


run_program()
