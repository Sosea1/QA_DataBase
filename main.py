import mysql.connector
from faker import Faker
import time

# Создаем экземпляр Faker для генерации случайных данных
fake = Faker()

def select_rows_count(cnx):
    cursor = cnx.cursor()
    query = "SELECT COUNT(*) FROM test_table"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return int(result)

# Функция для вставки одной записи
def insert_one_record(id, cnx):
    # Создаем курсор
    cursor = cnx.cursor()
    text = fake.text(max_nb_chars=200)
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO test_table (id, test_text, date) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, text, date))

# Генерация и вставка 10 миллионов записей
def insert_all_records(cnx, rows_):
    for i in range(1, rows_+1):
        start_time = time.time()
        insert_one_record(i, cnx)
        # После каждых 10000 записей делаем коммит, чтобы освободить память
        if i % 10000 == 0:
            cnx.commit()
            print(f"Committed after {time.time() - start_time} seconds")

def main(cnx):
    rows_number = 10_000_000
    rows_ = rows_number - select_rows_count(cnx)
    insert_all_records(cnx, rows_)

if __name__ == '__main__':
    cnx = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='test')
    main(cnx)
    cnx.close()