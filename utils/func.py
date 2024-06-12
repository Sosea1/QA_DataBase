# Создание тестовой таблицы
def create_table(connection):
    cursor = connection.cursor()
    query = """CREATE TABLE IF NOT EXISTS test_table (
    id int NOT NULL AUTO_INCREMENT,
    test_text varchar(255) DEFAULT NULL,
    date datetime DEFAULT NULL,
    PRIMARY KEY (id)
    )"""
    cursor.execute(query)


# Вывести количество строк
def select_rows_count(connection):
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM test_table"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return int(result)


# Создать индекс для столбца
def create_index(connection):
    cursor = connection.cursor()
    query = "CREATE INDEX test_text_idx ON test_table(test_text)"
    cursor.execute(query)
    connection.commit()


# Убрать индекс для столбца
def drop_index(connection):
    cursor = connection.cursor()
    query = "DROP INDEX test_text_idx ON test_table"
    cursor.execute(query)
    connection.commit()


# Получить все записи по запросу
# Можно было еще добавить передачу патерна, но тогда каждый раз прописывать его не охото было
def select_all(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM test_table WHERE test_text LIKE %s"
    pattern = 'Already%'
    cursor.execute(query, (pattern,))
    rows = cursor.fetchall()
    return rows
