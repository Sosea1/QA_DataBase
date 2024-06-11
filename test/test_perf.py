import time
import mysql.connector
import pytest
from utils.func import select_all, create_index, drop_index


# Фикстура, создание окружения, в данном случае подключение к БД
@pytest.fixture(scope="session", autouse=True)
def test_db():
    connection = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='test')
    yield connection
    connection.close()


# Тест производительности запроса без индекса
def test_perfomance_select_like_no_index(test_db, benchmark):
    connection = test_db
    benchmark(select_all, connection)


# Тест производительности запроса с индексом
def test_perfomance_select_like_index(test_db, benchmark):
    connection = test_db
    create_index(connection)
    benchmark(select_all, connection)
    drop_index(connection)

