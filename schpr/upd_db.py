import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('comp.db')  # Убедитесь, что путь к вашей базе данных правильный
cursor = conn.cursor()


# Функция для создания новой таблицы с первичным ключом
def create_new_table():
    # Создание новой таблицы nv
    cursor.execute("""
    CREATE TABLE nv_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    );
    """)

    # Создание новой таблицы rd
    cursor.execute("""
    CREATE TABLE rd_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    );
    """)

    # Создание новой таблицы rizen
    cursor.execute("""
    CREATE TABLE rizen_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        motherboard TEXT,
        price INTEGER
    );
    """)

    # Создание новой таблицы intel
    cursor.execute("""
    CREATE TABLE intel_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        motherboard TEXT,
        price INTEGER
    );
    """)

    # Создание новой таблицы otherset
    cursor.execute("""
    CREATE TABLE otherset_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cooler TEXT,
        RAM TEXT,
        bp TEXT,
        priceSum INTEGER
    );
    """)


# Функция для копирования данных из старых таблиц в новые
def copy_data():
    # Копирование данных из nv
    cursor.execute("INSERT INTO nv_new (model, price) SELECT model, price FROM nv;")

    # Копирование данных из rd
    cursor.execute("INSERT INTO rd_new (model, price) SELECT model, price FROM rd;")

    # Копирование данных из rizen
    cursor.execute("INSERT INTO rizen_new (model, motherboard, price) SELECT model, motherboard, price FROM rizen;")

    # Копирование данных из intel
    cursor.execute("INSERT INTO intel_new (model, motherboard, price) SELECT model, motherboard, price FROM intel;")

    # Копирование данных из otherset
    cursor.execute(
        "INSERT INTO otherset_new (cooler, RAM, bp, priceSum) SELECT cooler, RAM, bp, priceSum FROM otherset;")


# Функция для удаления старых таблиц и переименования новых
def replace_old_tables():
    cursor.execute("DROP TABLE nv;")
    cursor.execute("DROP TABLE rd;")
    cursor.execute("DROP TABLE rizen;")
    cursor.execute("DROP TABLE intel;")
    cursor.execute("DROP TABLE otherset;")

    cursor.execute("ALTER TABLE nv_new RENAME TO nv;")
    cursor.execute("ALTER TABLE rd_new RENAME TO rd;")
    cursor.execute("ALTER TABLE rizen_new RENAME TO rizen;")
    cursor.execute("ALTER TABLE intel_new RENAME TO intel;")
    cursor.execute("ALTER TABLE otherset_new RENAME TO otherset;")


# Выполнение всех шагов
try:
    create_new_table()  # Создаем новые таблицы
    copy_data()  # Копируем данные в новые таблицы
    replace_old_tables()  # Удаляем старые и переименовываем новые

    print("Все операции выполнены успешно.")
except sqlite3.Error as e:
    print(f"Ошибка при выполнении операций: {e}")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

