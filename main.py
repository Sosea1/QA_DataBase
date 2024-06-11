import mysql.connector
from faker import Faker
import time
from utils.func import select_rows_count

# Экземпляр класса для работы с методами генерации рандомных данных 
fake = Faker()


# Подготовка одной записи
def insert_record(id, connection):
    # Создаем курсор
    cursor = connection.cursor()
    text = fake.text(max_nb_chars=200)
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO test_table (test_text, date) VALUES (%s, %s)"
    cursor.execute(query, (text, date))


# Вставить заданное количество строк 
def insert_all_records(connection, rows_):
    for i in range(1, rows_+1):
        insert_record(i, connection)
        if i % 10000 == 0:
            connection.commit()
            print(f"Committed {i} rows")


def main(connection):
    rows_number = 10_000_000
    rows_ = rows_number - select_rows_count(connection)
    insert_all_records(connection, rows_)


if __name__ == '__main__':
    connection = mysql.connector.connect(user='root', password='1234',
                                         host='localhost',database='test')
    main(connection)
    connection.close()
